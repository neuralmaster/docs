# Common Pipeline

There are a vast number of different workflows with NeuralMaster, 
which depend on your task (creating a full texture for a model or refining details of an existing texture),
your working pipeline, style, and many other details.
The author believes he knows only a small portion of the possible options and hopes that users will find many of their own techniques.   

Below is one of the possible pipelines, combining different techniques.  
And here is a video using this pipeline.

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
  <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" 
          src="https://www.youtube.com/embed/b9qeVCmwJ2c" 
          frameborder="0" 
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
          allowfullscreen>
  </iframe>
</div>
<br>
## 1. Create the First Texture Layer - Main View of the Model

The task - to texture as much area of the model as possible with one frame.

1. Use txt2img mode (if there is no initial texture) or img2img (if there is a texture).
2. Work with the image as if it's symmetrical (in most cases this is possible).
3. Use an orthogonal camera.
4. Use Depth+Normal masks to achieve alignment of the model and texture.
5. Set a reference picture (using IP Adapter Plus) from a suitable perspective and/or use Lore and/or use a strong prompt. 
6. Strive for high resolution. 
7. Perform more iterations.
8. Adjust the correct layer parameters to apply the texture to both halves of the model.

This is where the work of other texturing tools based on NN/ML ends, but we will go further!

## 2. Second Layer - Fix Color Problems between the Two Halves of the Texture

The task - to correct color stitching problems due to the use of the txt2img mode.  
This step is effective if the first step used txt2img mode.

1. Use img2img mode.
2. Use the same orthogonal camera.
3. Set the render background color close to the desired color of the junction.
4. Use the same SD settings (prompts, seed, ControlNet masks, etc.).
5. Create a frame and obtain the texture.
6. Arrange the textures in reverse order, so the texture from the previous step overlays on top everywhere.
7. Adjust the Normals Angle mask threshold of the second layer to make the junction look correct.

## 3. Lift up the quality of the border of left and right halves

The task - to improve the junction of textures, achieve a more accurate texture pattern and color.

1. Use the inpaint mode.
2. Position the camera at the plane of texture junction and choose an angle as perpendicular to the surface of the model as possible.
3. Use an orthogonal camera.
4. Use Depth+Normal masks.
5. Set a reference picture (using ControlNet IP Adapter Plus) from a suitable perspective and/or use Lore and/or use a strong prompt.
6. Carefully select the inpainting area to avoid spoiling parts of the texture that are already well-drawn.
7. Try inpainting modes **Fill** and **Original**.
8. Perform many iterations, saving successful ones, and making new iterations on top. Always use the same inpaint mask.
9. Do not try to achieve a perfect generation result from a single iteration.
10. When the texture pattern is correct (but the color is still not right), connect ControlNet Canny and continue iterations - 
this will fix the pattern but allow trying different color options.

It is necessary to make several such frames from different camera perspectives to cover the perimeter of the junction.

## 4. Create a Reference Texture for Refining Micro-Detail of the Model's Texture

The task - to create a mask for refining micro-details of the texture (e.g., drawing the fur of an animal).

1. Find a large area on the model with significant texture but minimal color variation, predominantly albedo.
2. Take a screenshot of such a maximized area, save it as a file, upload it to Blender.

## 5. Enhance Micro-Details of the Texture Using the Reference Mask

The task - to draw micro-details.

1. Use the Inpaint mode.
2. Use the created image as a reference mask for ControlNet IP Adapter Plus.
3. Choose the camera so that the required scale and direction of micro-details in the frame roughly match the reference.
4. Use a resolution (and, accordingly, camera scale) approximately matching the resolution of the reference mask.
5. Create multiple shots to texture all incorrect areas.
6. If necessary, rotate and flip the reference image in the ControlNet input parameters.
7. Take many shots to correct all visible texture defects.

## 6. Texture Individual Distinctive Details of the Model

The task - to draw individual unique details of the model that require more detail, such as the head, legs, etc.

1. Take multiple shots to correct all visible texture defects.
2. Position the camera perpendicular to the surface, and use an orthographic camera if possible.
3. Combine techniques from previous layers: reference masks, lore, strong prompts, symmetrical texturing, etc.
4. Adjust layer parameters ('Depth' and 'Normals Angle' masks) to avoid unwanted influence the new layer to previous. 
For example, when texturing an animal's head, it is convenient to use depth mask cutoff to avoid accidentally spoiling the already textured legs and shoulders.
5. Utilize techniques of symmetrical texturing.

## 7. Periodically Bake Texture Layers into a Single Combo Layer

1. Use the layer editor.
2. Select the necessary layers, sort them if necessary.
3. Press the baking button.

## Bonus! Create a Video Visualizing the Texturing Process Using Player

1. Make a backup of the Blend file.
2. Set the start and end layers of the video, and the number of frames per layer.
3. In the layer editor, disable the layers that need to be skipped (usually, all fusion layers).
4. Use Play for a preliminary review of the video.
5. Use Rec to record the video as a sequence of frame-png files.
6. Use Blender Sequencer to combine png files into a single avi file.
