import os, shutil, requests, subprocess
from tqdm import tqdm

def delete_and_clone_git_repo(repo_url, target_folder):
    """
    Deletes the existing directory (if it exists) and clones a Git repository into that folder.

    :param repo_url: URL of the Git repository to be cloned.
    :param target_folder: Path where the repository should be cloned.
    """
    # Check if the directory exists
    if os.path.exists(target_folder):
        # Delete the directory
        print(f"Deleting existing directory: {target_folder}")
        shutil.rmtree(target_folder)

    # Clone the repository
    print(f"Cloning repository to {target_folder}...")
    subprocess.run(["git", "clone", repo_url, target_folder])
    print(f"Cloning complete")


def download_files(base_url, base_dst_folder, file_map, overwrite_existing=False):
    if not os.path.exists(base_dst_folder):
        os.makedirs(base_dst_folder)

    for src_filename, dst_filename in tqdm(file_map.items(), desc="Processing files"):
        dst_path = os.path.join(base_dst_folder, dst_filename)

        # Skip download if file already exists
        if os.path.exists(dst_path) and not overwrite_existing:
            print(f"'{dst_path}' already exists. Skipping download.")
            continue

        url = base_url + src_filename
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()

            total_size_in_bytes = int(response.headers.get('content-length', 0))
            block_size = 1024  # 1 Kibibyte

            progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True, desc=f"Downloading {src_filename}")
            with open(dst_path, 'wb') as f:
                for data in response.iter_content(block_size):
                    progress_bar.update(len(data))
                    f.write(data)
            progress_bar.close()

            if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
                print(f"ERROR, something went wrong downloading '{src_filename}'")

        except requests.exceptions.HTTPError as err:
            print(f"HTTP Error: {err} for file '{src_filename}'")
        except Exception as e:
            print(f"Error downloading '{src_filename}': {e}")


url_sd15 = "https://huggingface.co/h94/IP-Adapter/resolve/main/models/"
url_sdxl = "https://huggingface.co/h94/IP-Adapter/resolve/main/sdxl_models/"

dst_folder = "/workspace/sd/stable-diffusion-webui/extensions/sd-webui-controlnet/models/"

files_sd15_safetensors = {
    "ip-adapter-full-face_sd15.safetensors": "ip-adapter-full-face_sd15.safetensors",
    "ip-adapter-plus-face_sd15.safetensors": "ip-adapter-plus-face_sd15.safetensors",
    "ip-adapter-plus_sd15.safetensors": "ip-adapter-plus_sd15.safetensors",
    "ip-adapter_sd15.safetensors": "ip-adapter_sd15.safetensors",
    "ip-adapter_sd15_light.safetensors": "ip-adapter_sd15_light.safetensors",
    "ip-adapter_sd15_vit-G.safetensors": "ip-adapter_sd15_vit-G.safetensors",
}

files_sd15_bin = {
    "ip-adapter-full-face_sd15.bin": "ip-adapter-full-face_sd15.pht",
    "ip-adapter-plus-face_sd15.bin": "ip-adapter-plus-face_sd15.pht",
    "ip-adapter-plus_sd15.bin": "ip-adapter-plus_sd15.pht",
    "ip-adapter_sd15.bin": "ip-adapter_sd15.pht",
    "ip-adapter_sd15_light.bin": "ip-adapter_sd15_light.pht",
    "ip-adapter_sd15_vit-G.bin": "ip-adapter_sd15_vit-G.pht",
}

files_sdxl_safetensors = {
    "ip-adapter-plus-face_sdxl_vit-h.safetensors": "ip-adapter-plus-face_sdxl_vit-h.safetensors",
    "ip-adapter-plus_sdxl_vit-h.safetensors": "ip-adapter-plus_sdxl_vit-h.safetensors",
    "ip-adapter_sdxl.safetensors": "ip-adapter_sdxl.safetensors",
    "ip-adapter_sdxl_vit-h.safetensors": "ip-adapter_sdxl_vit-h.safetensors",
}

files_sdxl_bin = {
    "ip-adapter-plus-face_sdxl_vit-h.bin": "ip-adapter-plus-face_sdxl_vit-h.pht",
    "ip-adapter-plus_sdxl_vit-h.bin": "ip-adapter-plus_sdxl_vit-h.pht",
    "ip-adapter_sdxl.bin": "ip-adapter_sdxl.pht",
    "ip-adapter_sdxl_vit-h.bin": "ip-adapter_sdxl_vit-h.pht",
}

download_files(url_sd15, dst_folder, files_sd15_safetensors)
#download_files(url_sdxl, dst_folder, files_sdxl_safetensors)

nm_inpainter_repo_url = "https://github.com/neuralmaster/neuralmaster_inpainter.git"
nm_inpainter_target_folder = "//workspace/sd/stable-diffusion-webui/extensions/nm_inpainter"
delete_and_clone_git_repo(nm_inpainter_repo_url, nm_inpainter_target_folder)
