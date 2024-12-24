# Neural Master

## What is this?

Neural Master is an unique AI texturing Blender addon based on Stable Diffusion

The addon can be used to fully texturize a model, which is especially important for indie developers, neural art fans and beginning artists.

Professionals can use it to refine details of complex diffuse textures or to create a rough source texture to save time.

The addon can also be used for projection texturing and for baking.

## **Download from [Gumroad](https://nmaster.gumroad.com/l/neuralmaster) or [Blendermarket](https://blendermarket.com/products/neuralmaster)** 

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
  <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" 
          src="https://www.youtube.com/embed/LoVL5KHSW5Q"
          frameborder="0" 
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
          allowfullscreen>
  </iframe>
</div>

<br>

## How to use

### Take the first shot:  
1. Set the camera  
2. Select a reference image (if it is) and whire a ptompt   
3. Take a shot. Rolls several iteration if it is required

![First shot](../gif/chest_first_shot.gif)

### Turn the camera and take another shot

![Second shot](../gif/chest_second_shot.gif)

### Do this several times

![Several shots](../gif/chest_several_shots.gif)

### Bake the resulted texture

![Bake](../gif/chest_fusion.gif)

## Key Features

1. Step by step texturing process by moving camera and creating shots using Stable Diffusion (see above).

2. Using reference images instead of (in addition to) text prompts (see above).

3. Auto-generated inpainting masks, that allow you to save time.
    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
      <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" 
              src="https://www.youtube.com/embed/rRapGndqD-4"
              frameborder="0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen>
      </iframe>
    </div>
    <br>

4. High quality inpainting using 'Neural Master Inpainter' extension for Stable Diffusion.
    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
      <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" 
              src="https://www.youtube.com/embed/Y2RMvgzrEc8"
              frameborder="0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen>
      </iframe>
    </div>
    <br>

5. Auto settings (especially important for beginners).

6. Detailed customization (for advanced users).

7. Convenient tools for baking resulted  texture.

8. Working with a remote Stable Diffusion server, not just a local one.

9. And much more.

## Current stage of the project

The adon is in open beta - it is quite complete and really simplifies the texturing process in many cases, and is also stable enough to use by external users.

At the same time, I need feedback from users, as much feedback as possible, in order to make the addon better and adapt it to tasks that are truly relevant to users, and, together with them, develop the best texturing pipelines.

Please do not hesitate to write your bugreports, featurequests and feedback. Everything will be analyzed, prioritized, added to the plan and implemented.

Right now it's difficult to give an exact release date, but it is expected to take place in the first quarter of 2024.

## Plans

Nearest plans:

1. Bugfix and polishing based on your feedback.
2. Feature: generation of several images from SD in one request and local saving of all previously generated images.
3. Feature: multi-view mode, which allows you to shoot a 3d model from several different views in one shot.

Plans will change in accordance with your feedback and the development of technologies and trends in neuroart, but one thing will remain unchange: we will try to achieve the greatest possible control over generation, and not reduce everything into a one-button solution.
