# Setup Deep Geometric Prior in docker container

1. apt update
2. apt install git -y
3. apt install wget -y
4. apt install unzip -y
5. git clone https://github.com/montehoover/deep-geometric-prior.git
6. wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
7. bash https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
8. Read license, type yes, hit enter a few times
9. cd deep-geometric-prior
10. conda env create -f environment.yml
11. conda activate deep-geometric-prior
12. conda install -c conda-forge gdown -y
13. gdown https://drive.google.com/uc?id=17Elfc1TTRzIQJhaNu5m7SckBH_mdjYSe
14. unzip deep_geometric_prior_data.zip
15. python reconstruct_surface.py deep_geometric_prior_data/scans/gargoyle.ply 0.01 1.0 20 -d cuda:0 cuda:1 cuda:2 cuda:3 -nl 25 -ng 25 -o gargoyle
