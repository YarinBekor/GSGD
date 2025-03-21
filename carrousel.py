from PIL import Image
import os
import numpy as np

def create_carousel_gif(folder_path, output_path='carousel.gif'):
    """
    Creates a carousel GIF by taking the i-th frame from the i-th GIF in the input folder.
    Selects exactly 14 evenly spaced GIFs from the collection.
    Output GIF runs at 10 FPS (100ms per frame).
    """
    # Get all GIF files from the folder and sort by angle number
    gif_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.gif')]
    gif_files.sort(key=lambda x: int(x.split('_')[1].split('.')[0]))
    gif_files = gif_files * 16
    
    # Always select exactly 14 evenly spaced indices
    # indices = np.linspace(0, len(gif_files) - 1, 14, dtype=int)
    # gif_files = [gif_files[i] for i in indices]
    
    print(f"Selected files: {gif_files}")
    
    if not gif_files:
        raise ValueError("No GIF files found in the specified folder")

    frames = []
    
    # Process each GIF file
    for i, gif_file in enumerate(gif_files):
        gif_path = os.path.join(folder_path, gif_file)
        with Image.open(gif_path) as img:
            # Check if image is animated and get number of frames
            n_frames = getattr(img, 'n_frames', 1)
                
            # Skip to the i-th frame (or i-14-th frame if i>=14)
            frame_idx = i if i < 14 else i % 14
            for _ in range(min(frame_idx, n_frames - 1)):
                img.seek(img.tell() + 1)
                
            # Get the current frame
            current_frame = img.copy()
            frames.append(current_frame)

    if not frames:
        raise ValueError("No frames were extracted from the GIF files")

    # Save the carousel GIF with 100ms duration (10 FPS)
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=110,  # 100ms per frame = 10 FPS
        loop=0,
        optimize=True
    )


create_carousel_gif('/home/yarinbekor/Desktop/THESIS/Junk_VIS/19.3/dumbo', 'static/videos/bird/dynamic_carousel.gif')