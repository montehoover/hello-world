import torch
from torch import nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from more_itertools import peekable

# A good resource is here: https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html#training-a-classifier

EPOCHS = 10
BATCH_SIZE = 128
ETA = 0.001


class MLP(nn.Module):
    def __init__(self, input_shape, num_classes):
        super(MLP, self).__init__()
        # # Expect input_shape of 3-dim: Channels x H x W
        self.fc1 = nn.Linear(input_shape[0] * input_shape[1] * input_shape[2], 84)
        self.fc2 = nn.Linear(84, 50)
        self.fc3 = nn.Linear(50, num_classes)
    
    def forward(self, x):
        x = torch.flatten(x, 1) # flatten all dimensions except batch
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        # Output. Return logits directly intead of softmax since our loss function will calculate softmax.
        return x


class CNN(nn.Module):
    def __init__(self, input_shape, num_classes):
        super(CNN, self).__init__()
        # Expect input_shape of 3-dim: Channels x H x W
        self.conv1 = nn.Conv2d(input_shape[0], 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 4 * 4, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, num_classes)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = torch.flatten(x, 1) # flatten all dimensions except batch
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        # Output. Return logits directly intead of softmax since our loss function will calculate softmax.
        return x


def train(model, dataloader, load_from_weights=False):
    if load_from_weights:
        model.load_weights('cnn.pth')
    else:
        trainloader, testloader = dataloader
        loss_fn = nn.CrossEntropyLoss()
        optim = torch.optim.Adam(model.parameters(), lr=ETA)
        device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Using {device} device")
        for epoch in range(EPOCHS):  # loop over the dataset multiple times
            train_loss = 0
            val_loss = 0
            num_correct = 0
            for batch in trainloader:
                inputs, targets = batch
                inputs = inputs.to(device)
                targets = targets.to(device)
                model = model.to(device)
                # reset the parameter gradients before starting backward pass
                optim.zero_grad()
                # forward + backward + optimize
                outputs = model(inputs)
                loss = loss_fn(outputs, targets)
                loss.backward()
                optim.step()
                train_loss += loss.item()
            train_loss = train_loss / BATCH_SIZE

            model.eval()
            num_correct = 0 
            num_examples = 0
            for batch in testloader:
                inputs, targets = batch
                inputs = inputs.to(device)
                targets = targets.to(device)
                model = model.to(device)
                output = model(inputs)
                loss = loss_fn(output,targets) 
                val_loss += loss.item()
                correct_arr = torch.eq(torch.max(F.softmax(output, dim=1), dim=1)[1], targets)
                num_correct += torch.sum(correct_arr).item()
            val_loss = val_loss / BATCH_SIZE
            acc = num_correct / len(testloader.dataset)
            print(f"Epoch {epoch + 1} train_loss: {train_loss:.3f},  val_Loss: {val_loss:.3F}, accuracy = {acc:.3f}")
        print('Finished Training')
        torch.save(model.state_dict(), 'cnn.pth')
    return model


def get_data(dataset):
    if dataset == 'cifar10':
        transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
        ])
        trainset = datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
        testset = datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)

    elif dataset == 'mnist':
        transform = transforms.Compose([
            transforms.ToTensor()
        ])
        trainset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
        testset = datasets.MNIST(root='./data', train=False, download=True, transform=transform)
    
    trainloader = DataLoader(trainset, batch_size=BATCH_SIZE, shuffle=True, num_workers=2)
    testloader = DataLoader(testset, batch_size=BATCH_SIZE, shuffle=False, num_workers=2)
    # Weird pytorch thing: The MNIST DataSet object (trainset) does not have a channel dimension (shape = 28 x 28).
    # However the DataLoader object (trainloader) adds a channel dimension for us automatically (shape = 1 x 28 x 28).
    # So we need to be sure to use trainloader when looking for the input_shape that will be used at training time.
    X_batch, y_batch = peekable(trainloader).peek()
    input_shape = X_batch[0].shape
    num_classes = len(trainset.classes)
    dataloader = trainloader, testloader
    return dataloader, input_shape, num_classes


if __name__ == '__main__':
    dataloader, input_shape, num_classes = get_data('mnist')
    models = MLP(input_shape, num_classes), CNN(input_shape, num_classes)
    for model in models:
        model = train(model, dataloader)
        # Example of a single prediction with a trained model
        single_example = next(iter(dataloader[1]))[0][0:1]
        print(model(single_example))