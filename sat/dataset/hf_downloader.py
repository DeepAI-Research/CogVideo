import os
import argparse
from huggingface_hub import HfApi, hf_hub_download
from tqdm import tqdm

def download_dataset(repo_id, token=None, download_dir="./videos", num_files=None):
    # Initialize Hugging Face API client
    api = HfApi(token=token)
    
    # Create output directory if it doesn't exist
    os.makedirs(download_dir, exist_ok=True)
    
    # List all files in the repository
    files = api.list_repo_files(repo_id)
    
    # Limit the number of files if max_files is specified
    if num_files is not None:
        files = files[:num_files]
    
    # Download each MP4 file
    for file in tqdm(files):
        local_filename = os.path.join(download_dir, os.path.basename(file))
        
        hf_hub_download(
            repo_id=repo_id,
            filename=file,
            local_dir=download_dir,
            local_dir_use_symlinks=False,
            token=token
        )
        
        print(f"Downloaded {file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download dataset from HuggingFace Hub")
    parser.add_argument("--repo", type=str, default="DeepAIResearch/SpatialSceneSyntheticDataset", help="HuggingFace repository ID")
    parser.add_argument("--token", type=str, default="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", help="HuggingFace API token")
    parser.add_argument("--output", type=str, default="./videos", help="Output directory for downloaded files")
    parser.add_argument("--num_files", type=int, default=None, help="Maximum number of files to download (default: all)")
    
    args = parser.parse_args()

    download_dataset(args.repo, args.token, args.output, args.num_files)