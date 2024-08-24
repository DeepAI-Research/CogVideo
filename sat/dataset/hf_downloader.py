import os
import argparse
from huggingface_hub import HfApi, hf_hub_download
from tqdm import tqdm

def download_dataset(repo_id, token=None, num_files=100):
    # Initialize Hugging Face API client
    api = HfApi()
    download_dir="./videos"
    # Create output directory if it doesn't exist
    os.makedirs(download_dir, exist_ok=True)
    print(repo_id, token)

    # List all files in the repository
    files = [file for file in api.list_repo_files(repo_id=repo_id, token=token, repo_type="dataset") if file.endswith('.mp4')]    

    # Limit the number of files if max_files is specified
    if num_files is not None:
        files = files[:num_files]
    

    # Download each MP4 file
    for file in tqdm(files):
        
        hf_hub_download(
            repo_id=repo_id,
            repo_type="dataset",
            filename=file,
            local_dir=download_dir,
            local_dir_use_symlinks=False,
            token=token
        )
        
        print(f"Downloaded {file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download dataset from HuggingFace Hub")
    parser.add_argument("--repo", type=str, default="DeepAIResearch/SpatialSceneSyntheticDataset", help="HuggingFace repository ID")
    parser.add_argument("--token", type=str, default=None, help="HuggingFace API token")
    parser.add_argument("--num_files", type=int, default=100, help="Maximum number of files to download (default: all)")
    
    args = parser.parse_args()

    repo_id = "DeepAIResearch/SpatialSceneSyntheticDataset"
    download_dataset(repo_id, args.token, args.num_files)