# Basics

## General principles

Texturing using Neural Master is a sequential synthesis of the model’s texture from pictures, created from different views, and then combining them into a single texture.  
That is, the well-known, widespread technique of projection texturing is used here.
Such texture fragments are called **texture layers** in NeuralMaster.

To create the texture layer, you need to perform 2 operations: 

1. Set the camera to the desired position and render the model.  
2. Use Stable Diffusion to create a fragment of a texture.  

After creating the layer, you need to move the camera to a new area of the model, and create a new texture layer, etc.  
The layers are layered on top of each other sequentially to create an overall texture.

When creating each texture layer, it is very important to achieve the so-called **consistency**, that is, its correct joining with other texture layers so that the model looks uniform and harmonious.
Stable Diffusion was not originally designed to solve this problem, but there are a number of extensions for SD, as well as a number of techniques that allow you to achieve good consistency.  
Some of them are described in the [Common Pipeline](common_pipeline.md) section, as well as in the [FAQ](faq.md) section, which will be constantly updated.

After multiple layers are created, they are baked into one overall texture using the final UV coordinates.

## Creating a texture layer

### 1. Configure render parameters.

1. Texture layer type:  
**txt2txt** - frame generation only based on a text prompt. Typically used for the initial layer  
**img2img** - frame generation based on render. Often used for the initial layer, as well as for texturing symmetrical areas of the texture.  
**inpaint** - detailing of a frame fragment in the selected area.

2. Camera type, its parameters and position.  
2 camera types are supported - perspective and orthogonal.  
We recommend to use usually an orthogonal camera.  
Tips for setting this parameter are given in [FAQ](faq.md).
3. Render resolution.  
As a rule, it is better to use the resolution that is optimal for the selected Stable Diffusion model. See our recommendations in [FAQ](faq.md).
    
### 2. Click the Render layer button

At this stage, not only the diffuse texture render is created, but also many different masks for Stable Diffusion and for combining texture layers.
(see details in the description of the [Render Settings](panels/render_settings_panel.md) window).  
In addition, a special UV layer is created for the resulting image.

Render duration ranges from fractions to several tens of seconds, depending on the performance of your computer and the selected render parameters.
During this time, the main Blender thread will be blocked and it may appear frozen. This is normal, don't worry.

### 3. Configure Stable Diffusion generation parameters
 
Including: propmpt, negative prompt, seed, denoising strength, input image, inpaint mask, CFG Scale, ControlNet parameters and much more.
Currently, almost all parameters used in Automation are supported, except upscaler and refiner.
(some parameters cannot be configured through the NeuralMaster, however, they can be enabled via the website and used in NeuralMaster).

Please give the feedback what parameters of Stable Diffusion you would like to see in the NeuralMaster.

### 4. Click the Generate layer button

The button starts generation in Stable Diffusion.
This operation is also lengthy, and can last from seconds to several minutes, depending on the selected frame parameters,
in which the main Blender thread will be blocked and it may appear to be frozen.

### 5. Apply result

After generation, you need to look at the result, and if it is satisfactory, save it by clicking the Apply button.
If you are not satisfied with the result, you need to change the generation settings and click the Generate button again.
You can also cancel the layer at any time and return to the camera settings stage.

## Baking multiple layers into an overall texture

Baking texture layers into a single "fusion" layer is done in the [layer editor](panels/layers_panel.md).
The window displays a list of all texture layers created previously, and you can see that layers can be of 3 types:

1. **Initial** - the initial layer created when the NeuralMaster session was initialized
2. **Shot** - layer created using a neural network
3. **Fusion** - A layer obtained by baking a combination of several other layers

The checkboxes highlight exactly those texture layers that are currently displayed on the model.
By checking and unchecking the checkboxes, you can activate or deactivate each layer.

To create a new fusion layer, you need to check the required layers (as a rule, these are all layers of the Shot type,
as well as the one Initial or Fusion layer preceding them), and then press the fusion button.
After clicking the button, a pop-up window will appear where you need to select the resolution of the resulting texture.
The duration of the operation depends on the resolution of the selected texture and the performance of your video card, and can last from a second to several minutes.

After creating a shared layer, all baked Shot layers will be marked as archived and hidden from the list.
The UV coordinates of all these layers will also be removed, so new Shot layers can be created.

### Notes
1. Unfortunately, Blender does not allow you to create more than 8 UV coordinates for one mesh, so you need to bake the overall one after creating the 7th texture layers (the 8th UV will always be used for your final UV).
However, this is not burdensome and is even useful, since too many active texture layers can cause performance problems. And besides, when baking the texture into the final one, a loss of quality may occur, and therefore, it is sometimes useful to see the intermediate result.
2. All archived layers can be restored later, if necessary, as described in the description of the [layer editor](panels/layers_panel.md).