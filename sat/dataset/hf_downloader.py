import os
from huggingface_hub import HfApi, hf_hub_download
from tqdm import tqdm

def download_dataset(repo_id, token=None, download_dir="./downloaded_videos"):
    
    # Initialize Hugging Face API client
    api = HfApi(token=token)
    
    # Create output directory if it doesn't exist
    os.makedirs(download_dir, exist_ok=True)
    
    # List all files in the repository
    files = api.list_repo_files(repo_id)
    
    
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
    hf_repo = "DeepAIResearch/test_dataset"
    hf_token = "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"

    download_dataset(hf_repo, hf_token)