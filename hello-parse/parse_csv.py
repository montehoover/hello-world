import pandas as pd
import argparse

def run(args):
    df = pd.read_csv(args.input_file)
    
    # Grab a few rows, say the last three:
    # (use iloc if working with indexes)
    print(df.iloc[-4:-1])
    print()

    # Grab a couple columns based on their names:
    # (use loc if working with names)
    print(df.loc[:, ['label', 'youtube_id']])
    print()

    # Use itertuples to iterate over each row and do something based on column names:
    url_prefix = 'https://www.youtube.com/watch?v='
    with open('urls.txt', 'w') as f:
        for row in df.itertuples():
            url = url_prefix + row.youtube_id
            print(f"{row.label}: {url}", file=f)
    print("Wrote urls to urls.txt")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            description='''
                Read youtube ids from a file and return a file of full urls.
                ''')
    parser.add_argument("-i", "--input_file", default="data_csv/videos.csv", 
            help='''
                File with Youtube IDs to download.
                The file must be in csv format with the following header row:
                label, youtube_id, time_start, time_end, split
                ''')
    args = parser.parse_args()
    run(args)
