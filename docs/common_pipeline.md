## Note 2024-01-18 

This pipeline is outdated.  
Soon a new pipeline will be written here that uses the extension [**Neural Master Inpainter** for Automatic 1111](nm_inpainter/README.md) . 

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

1. txt2img or img2img mode.
2. Orthogonal camera.
3. Controlnet Depth + Normal 
4. Prompt + optional reference image (IP Adapter Plus) + optional Lora
5. Roll several iteration

![First frame](../gif/first_shot_png.gif)

This is where the work of other texturing tools based on NN/ML ends, but we will go further!

Показать создание первого кадра

## 2. Improve the Texture Quality at the Junction of Halves

1. Inpaint mode.
2. ControlNet Depth + Normal.
3. Prompt + optional reference image (IP Adapter Plus) + optional Lora.
4. Optional ControlNet Canny to fix desirable texture patern.
5. Roll several iteration

![Fill the border](../gif/second_shot_png.gif)

## 3. Create a Reference Texture for Refining Micro-Detail of the Model's Texture

1. Find a reference section of the finished texture.
2. Take a screenshot and save it.

![Create reference image](../gif/create_pattern_png.gif)

## 4. Enhance Micro-Details of the Texture Using the Reference Mask

1. Inpaint mode.
2. Use reference image (ControlNet IP adapter Plus).
3. Inpaint all the required fragments of the model.

![Inpaint by battern](../gif/inpaint_by_pattern_png.gif)

## 5. Add unique details using precise pattern

1. Inpaint mode
2. ControlNet: IP Adapter Plus, Scribblle, Depth
3. Prompt is important

![Wooden can logo](../gif/wooden_can_logo_png.gif)

## 6. Texture individual details of the Model

1. Combine techniques from previous suggestions.
2. Take many shots to correct all visible defects.

![Texture head](../gif/texture_head_png.gif)

## 7. Bake Texture Layers into a Single Combo Layer

1. Select the necessary layers using Layer editor.
2. Press the baking button.

![Fuse layers](../gif/make_fusion_layer_png.gif)
    
## Bonus! Create a Video Visualizing the Texturing Process

1. Set the start and end layers, and the number of frames per layer.
2. Preview video using Play button.
3. Record video to files.
