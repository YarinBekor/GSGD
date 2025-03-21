from PIL import Image
import os

def edit_gif(gif_path, top, bottom, left, right, fps, cut_frames=0):
    # Get the original file path and create new path with _new
    file_name, file_ext = os.path.splitext(gif_path)
    new_path = f"{file_name}_new{file_ext}"
    
    # Open the GIF
    original = Image.open(gif_path)
    
    # Get original size
    orig_width, orig_height = original.size
    
    # Extract all frames
    frames = []
    try:
        while True:
            # Copy the current frame
            frame = original.copy()
            # Crop the frame according to specifications
            # The crop coordinates are (left, top, right, bottom)
            frame = frame.crop((left, top, orig_width - right, orig_height - bottom))
            frames.append(frame)
            original.seek(original.tell() + 1)
    except EOFError:
        pass  # We've reached the end of the frames

    # Remove the specified number of frames from the end
    if cut_frames > 0:
        frames = frames[:-cut_frames]

    # Print number of frames
    print(f"Total frames in GIF: {len(frames)}")

    # Save the modified GIF
    frames[0].save(
        new_path,
        save_all=True,
        append_images=frames[1:],
        duration=int(1000 / fps),  # Convert fps to milliseconds
        loop=0
    )

if __name__ == "__main__":
    # Example usage
    gif_path = "static/videos/bird/bird_only_33.75.gif"
    top = 0      # how many pixels to crop from top
    bottom = 105   # how many pixels to crop from bottom
    left = 250     # how many pixels to crop from left
    right = 250    # how many pixels to crop from right
    fps = 10      # desired frames per second

    gif_path = "static/videos/bird/dambo_only_33.75.gif"
    top = 180      # how many pixels to crop from top
    bottom = 185   # how many pixels to crop from bottom
    left = 125     # how many pixels to crop from left
    right = 180    # how many pixels to crop from right
    fps = 10      # desired frames per second

    gif_path = "static/videos/bird/dambo_only_213.75.gif"
    top = 230      # how many pixels to crop from top
    bottom = 175   # how many pixels to crop from bottom
    left = 220     # how many pixels to crop from left
    right = 75    # how many pixels to crop from right
    fps = 10      # desired frames per second
    
    gif_path = "static/videos/bird/bird_only_213.75.gif"
    top = 0      # how many pixels to crop from top
    bottom = 120   # how many pixels to crop from bottom
    left = 300     # how many pixels to crop from left
    right = 230    # how many pixels to crop from right
    fps = 10      # desired frames per second

    gif_path = "static/videos/car/horse_only_90.00.gif"
    top = 0      # how many pixels to crop from top
    bottom = 120   # how many pixels to crop from bottom
    left = 230     # how many pixels to crop from left
    right = 230    # how many pixels to crop from right
    fps = 10      # desired frames per second
    cut_frames = 3

    gif_path = "static/videos/bird/dynamic_carousel.gif"
    top = 180      # how many pixels to crop from top
    bottom = 175   # how many pixels to crop from bottom
    left = 120     # how many pixels to crop from left
    right = 130    # how many pixels to crop from right
    fps = 10      # desired frames per second
    cut_frames = 0
    
    edit_gif(gif_path, top, bottom, left, right, fps, cut_frames)
