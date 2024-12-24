# FAQ

### In what cases is it appropriate to use Neural Master?

1. Creating a complex diffuse texture with irregular uncommon image such as, for example, used here for texturing a [knitted tiger](https://www.youtube.com/watch?v=b9qeVCmwJ2c).
2. Transfer sketches and/or references image to the texture of the model when it's difficult to use them as exact pattern for projecting texturing 
(because it is not exactly the same as the model) but it can be used as reference for neural network.  
3. Texturing of texture joints (using the inpainting method), where you want to create a smooth transition from one texture to another.
4. If you have very good skills in neural art, but you want to add a new dimension to your creativity and increase your capabilities by an order of magnitude. 
5. You are not so good at drawing, but would like to create a hand-drawn texture, such as creating an anime-style texture or impressionism or naive art.
6. You want to speed up the process of texturing multiple objects in a consistent style for your product,
for which you have many prepared sketches or references.

### In what cases is it inappropriate to use Neural Master?

1. Texturing of thin objects, such as thin spider legs, wires, etc.
2. Texturing highly transparent and reflective objects.
3. Texturing by homogeneous material, which are better done procedurally.
4. Creation overlapped textures (that sometimes is very important for optimizing performance and your work), for example for texturing tree leaves, tiled surfaces, etc.
5. Creation of typical objects of class for which there are high-quality specialized generators, for example, models of people or models of trees.

**Examples**

1. You need to create a **forest of trees**. There is no point in using Neural Master to create a large number of trees,
branches and leaves of trees, which have many regular (not unique) details.
Use specialized tree generators. However, for texturingg a thick tree trunk or some unique details on it 
(for example, details of tree bark or numbers cut out with a knife), Neural Master will be an effective tool.

2. **3D model of a character**. There are excellent character generators that create models with the necessary proportions, 
the most important details, skeleton, rig, face shapes and a set of materials. Use such character generator, they are effective tools. 
But then you need to add some details to make the model more unique and/or maybe stylize it. You can use Neural Master to do it.

### My computer is not very powerful. Can I use Neural Master?

Yes, you can.

1. Neural Master uses really light render settings, and if you use Blender for your work, most likely your computer is more than enough.

2. As for Stable Diffusion, there is absolutely no point in running it locally on your computer; instead, use cloud services for this, because at least:  

    - Cloud services are cheap. If you use neural art occasionally, then you are unlikely to pay even $10 a month for it.
        Even if Stable Diffusion is one of your main tools, the price is unlikely to be over $50. 
        And in both cases, you will use cloud servers with specialized GPUs like the A4500 or even A5000, which cost thousands of dollars.

    - You don't need to spend your time deploying Stable Diffusion locally and understanding this process, if you use a ready-made cloud environment.
            Your only need is to choose the most convenient cloud service for you and read the short instruction on how to launch Stable Diffusion.

    - You can use cloud services today instead of waiting until you can afford an expensive personal GPU card. It's a really simple and cheap way to try neural art.
      
    - Cloud hosting allow to use different hardware/software configurations depending on your task. 

### How to launch Stable Diffusion

Use [the instruction](how_to_install_sd.md) 


1. To lauch it on remote host use the instruction on the site of [Automatic 1111 WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Online-Services).  
This page contains the lists of supported services and the links to the instruction how to launch Stable Diffusion on them.

2. To launch SD on local computer use this instruction on the site of [Automatic 1111 WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui?tab=readme-ov-file)
 
### What is the best and cheapest way to use Stable Diffusion?

It is difficult to give the exact answer because it is required to make a detailed research to answer it, and also the answer depend on your needs.
I hope that thanks to the users I will be able to write this section in more detail and here you will find comprehensive 
information about local hosting and different hosting providers, but now I can give only some initial tips about one provider.
This is not an advertisement, there is simply no other information yet.

1. Don't use localhost because the hardware is too expensive and also cloud hosting allow to use different configuration depending on the task, and it launches immediately. 
(If you have such hardware and use local host then you are not the audience of this question, and you know enough about SD).
2. Theoretically it is existing the way to launch SD for free on Google Colab service, and everybody did it a year ago, 
but Google has changed the rules of using Colab, and seems it's impossible now to host SD server using Colab. Maybe some church exists, but I don't know, sorry.
3. Fortunately paid alternatives exist and they are cheap and more convenient. After inaccessibility of Colab, I made a personal research and found [RunPod](https://www.runpod.io/), that I've been using since then.
4. I'm not claiming that this service is the best, and this is not an advertisement. 
My research was done 8-10 months ago and RunPod was great because of good pricing and good quality, but now the situation may have changed and other services may not be more expensive and also of better quality. But the price and quality still suit me, and I don’t have time for new research yet.
5. I usually use [Community Cloud Server](https://www.runpod.io/console/gpu-cloud), choose the server A4500 (20 GB VRAM & 29 GB RAM) of $0.21 per hour 
and launch the image Stable Diffusion (runpod/stable-diffusion:fast-stable-diffusion-2.4.0) because it contains all the most important Stable Diffusion models and extensions.
Somtimes A4500 is inaccessible and I use A5000 (it is a rocket but the price is more - 29 cents) or somtimes 3090 (in my experience it is worse but the price is also more). 
Very seldom all the servers of Community type are busy and I use the servers of Secure Cloud but the price is significantly more (36 cents for A4500).
6. The environment Stable Diffusion(runpod/stable-diffusion:fast-stable-diffusion-2.4.0) launches jupiter notebook, and you can use it to launch Stable Diffusion.
It can look strange if you are not fluent in Python, but it is really convenient because the jupiter nodebook allow you to tune the SD before launch it.
7. If you use Runpod Community Cloud always choose Extreme internet speed to avoid long waiting for downloading. 
8. Don't forget stop cloud server when you don't use it.
  
### What configuration of Stable Diffusion is required?

If you are an experienced user of Stable Diffusion and find some controversial and incorrect points in my suggestions bellow, please give me a feedback. 

Some Stable Diffusion components are indeed required, and some are optional.

#### Required SD components

1. Use SD 1.5 model or a model derived from it (for example, Deliberate, Photon or another). This version better than SDXL because SDXL does not supports Normal Map ControlNet models that is very important.
2. Depth ControlNet (exists for SD1.5 and SDXL) is required to the texture fits accurately on the model.
3. Normal map ControlNet (exists for SD1.5 only) is also required so texture fits accurately on the model, in combination with the depth map ControlNet. 
4. A set of IP adapters (exists for SD1.5 and SDXL) but primarily IP Adapter Plus are requred to use reference image.
6. Canny Edge ControlNet (exists for SD1.5 and SDXL) is often required to fix macro details when inpainting micro details. Also, it can be used to texture fits accurately on the model if you use SDXL but not SD 1.5 (In this case use Fresnel map as an input of Canny preprocessor).
7. Scribble Controlnet (exists for SD1.5 and SDXL) often can be used to add some details of texture as patterns for these details.

If you are using a Fast Stable Diffusion environment, which I recommend above, all of these details (an even more other ControlNet models) are already in the environment, except for IP Adapters.
You can use the following [Python script to download and deploy IP adapters](py/sd_deploy.py).
Please fix the destination folder in the script before running it.

#### Optional SD components

1. SDXL model. Use it if you need high resolution, that is usually the most important for teh first texture layer. 
SDXL don't support Normal Maps and so the texture will not fit so accurately on the model as SD15 can, but in many cases it's enough to use Depth map and Canny Edge ControlNet giving the Fresnel map to the preprocessor.    
1. ControlNet reference_only. This can also be used to add a reference image, but the IP Adapter Plus typically yields better results.
2. LoRA models. This is a perfect way to keep generation consistent, but creating LoRA requires additional work.
If you plan to use neural art regularly (which in my opinion is absolutely necessary today), you should study LoRA technology and create and use your own LoRA models.
3. Inpainting SD models (for example, a [model from Runway](https://huggingface.co/runwayml/stable-diffusion-inpainting/resolve/main/sd-v1-5-inpainting.ckpt)).
This often results in a really smooth and high-quality blend of textures, but usually the image is blurred and lacks interesting detail.
4. Custom SD models. Typically, neural artists use such models, rather than the original SD 1.5 or SDXL, because custom models, which are based on the original models, 
but created later and created by neural artists that use it and contain knowledge crucial for practical tasks.
However, I don't have specific information yet about how effective these models are for texturing, so I can recommend none of them as a required.
I hope that soon there will be new models more focused on texturing. 
