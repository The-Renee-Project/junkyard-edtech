from PIL import Image
import os

def combine_images(image1_path, image2_path, output_path):
    img1 = Image.open(image1_path)
    img2 = Image.open(image2_path)

    # Ensure both images have the same width
    target_width = min(img1.width, img2.width)
    
    # Resize images if necessary
    if img1.width != target_width:
        img1 = img1.resize((target_width, int(img1.height * target_width / img1.width)))
    if img2.width != target_width:
        img2 = img2.resize((target_width, int(img2.height * target_width / img2.width)))

    # Calculate the height of the combined image
    height = img1.height + img2.height

    # Create a new image with the calculated dimensions
    combined_img = Image.new('RGB', (target_width, height))

    # Paste the first image at the top
    combined_img.paste(img1, (0, 0))

    # Paste the second image below the first one
    combined_img.paste(img2, (0, img1.height))

    # Save the combined image
    combined_img.save(output_path)

def main():
    # Combine global memory bandwidth and transfer latency
    combine_images('global_memory_bandwidth.png', 'transfer_latency.png', 'clpeak_combined.png')

    # Combine integer performance and integer time
    combine_images('integer_perf.png', 'integer_time.png', 'integer_combined.png')

    # Combine single performance and single time
    combine_images('single_perf.png', 'single_time.png', 'single_combined.png')

if __name__ == "__main__":
    main()
