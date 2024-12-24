# FAQ

### In what cases is it appropriate to use Neural Master?

Use it if your case is one of the following:

1. Creating a complex diffuse texture with irregular uncommon image such as, for example, used here for texturing a [knitted tiger](https://www.youtube.com/embed/b9qeVCmwJ2c).
2. Transfer sketches or/and references image to the texture of the model when it's  difficult to use them as exact pattern for projecting texturing 
(because it is not exactly the same as the model) but it can be used as reference for neural network.  
3. Texturing of texture joints (using the inpainting method), where you want to create a smooth transition from one texture to another.
4. If you have very good skills in neural art, but you want to add a new dimension to your creativity and increase your capabilities by an order of magnitude. 
5. You are not so good at drawing, but would like to create a hand-drawn texture, such as creating an anime-style texture or impressionism or naive art.
6. You want to speed up the process of texturing multiple objects in a consistent style for your product,
for which you have prepared many sketches or references to represent it.

### In what cases is it inappropriate to use Neural Master?

1. Texturing of thin objects, for example, thin spider legs, wires, etc.
2. Texturing highly transparent and reflective objects.
3. Textured objects with homogeneous material, which is better done procedurally.
4. Your texture should overlap (and this is very important to optimize performance and your work), for example for texturing tree leaves, tiled surfaces, etc.
5. Creation of typical objects of class for which there are high-quality specialized generators, for example, models of people or models of trees.

**Examples**

1. You need to create a forest of trees. There is no point in using Neural Master to create a large number of trees,
branches and leaves of trees, having a lot of regular (not unique) this details.
Use specialized tree generators. But for texturing a thick tree trunk or some unique details on it 
(for example, details of tree bark or numbers cut out with a knife), Neural Master will be an effective tool.

2. You need to create a 3D model of the character. There are excellent character generators that create character models with the necessary proportions, 
the most important details, skeleton, rig, face shapes and a set of materials. Use such character generator, they are effective tools. 
But then you need to add some details to make the model more unique and/or maybe stylize it. You can use Neural Master to do it.

### My computer is not very powerful. Can I use Neural Master?

Yes, you can.

1. Neural Master use really light render settings and if you use Blender for you work, most likely your computer is more than enough.

2. As for Stable Diffusion, there is absolutely no point in running it locally on your computer, use cloud services for this, because:  
- Cloud services are cheap. If you use neural art occasionally, then you are unlikely to pay even $10 a month for it.
Even if Stable Diffusion is one of your main tools then unlikely the price will be > $50.   
In both cases you will use a cloud servers with specialized GPU like A4500 or even A5000, costing thousands of dollars.  
- You don't need to spend your time to deploy Stable Diffusion locally, and understand these process, because of you will use a ready-made cloud environment, do.
Your only need to choose the most convenient cloud service for you and read the short instruction how to launch Stable Diffusion.  
- You can use cloud services today but not tomorrow when you can foun the mony for expencive personal GPU card. It's the really simple and cheep way to try neural art.  

### How to launch Stable Diffusion

1. To lauch it on remote host use the instruction on the site of [Automatic 1111 WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Online-Services)
This page contains the lists of supported services and the links to the instruction how to launch Stable Diffusion on them.

2. To launch Stable Diffusion on local computer use the instruction on the site of [Automatic 1111 WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui?tab=readme-ov-file)
 
### What is the best and cheapest way to use Stable Diffusion?

I don't have the exact answer for this question because it is required a king of research, and also it's depend on your needs.  
But I can give you some initial tips if you are new in neural art:

1. Don't use local host because the hardware is too expensive (if you already have such hardware and use local host then you are not the audience of this question, and you know enough about SD).
2. Theoretically it is existing the way to launch SD for free on Google Colab service, and everybody did it a year ago, 
but Google has changed the rules of using Colab, and now it is not so easy. I don't use Colab now and I don't know how to do it. Maybe some church exists, but I don't know, sorry.
3. After inaccessibility of Colab, I made a personal research and found [RunPod service](https://www.runpod.io/), that I've been using for a year and using it now.
4. I'm not claiming that this service is the best, and this is not an advertisement. 
My research was made 8-10 months and RunPod was excellent because good pricing policy and good quality, but now the situation could have changed, and other services may not be more expensive and also high quality. But I am still satisfied with the price and quality, and so far there is no time for a new research.
5. I usually use [Community Cloud Server](https://www.runpod.io/console/gpu-cloud), choose the server A4500 (20 GB VRAM & 29 GB RAM) of $0.21 per hour 
and launch the image Stable Diffusion(runpod/stable-diffusion:fast-stable-diffusion-2.4.0) because it contains all the most important Stable Diffusion models and extensions.
Somtimes A4500 is inaccessible and I use A5000 (it is a rocket but the price is more - 29 cents) or somtimes 3090 (by my expectation it is worse but the price is also more). 
Very seldom all the servers of Community type are busy and I use the servers of Secure Cloud but the price is significantly more (36 cents for A4500).   
6. The environment Stable Diffusion(runpod/stable-diffusion:fast-stable-diffusion-2.4.0) launches jupiter notebook, and you can use it to launch Stable Diffusion.
It can look strange if you are not fluent in Python, but it is really convenient because the jupiter nodebook allow you to tune the SD before launch it. 

I hope that thanks to the users I will be able to write this section in more detail and reasoning.
  
### What configuration of Stable Diffusion is required?

If you are an experienced user of Stable Diffusion and find some controversial and incorrect points in my suggestions, please give me a feedback. 

Some Stable Diffusion components are indeed required, and some are optional.

#### Required SD components

1. Use SD 1.5 model or a model derived from it (for example, Deliberate, Photon or another). This version better than SDXL because SDXL does not supports Normal Map ControlNet models that is very important.
2. Depth ControlNet (exists for SD1.5 and SDXL) is required to the texture fits accurately on the model.
3. Normal map ControlNet (exists only for SD1.5) is also required to so texture fits accurately on the model, in combination with the depth map ControlNet. 
4. A set of IP adapters (exists for SD1.5 and SDXL) but primarily IP Adapter Plus are requred to use reference image.
6. Canny Edge ControlNet (exists for SD1.5 and SDXL) is often required to save texutre macro details when inpainting micro details. Also it can be used to texture fits accurately on the model if you use SDXL but not SD 1.5 (In this case use Fresnel map as an input of Canny preprocessor).
7. Scribble Controlnet (exists for SD1.5 and SDXL) often can be used to add some details of texture as a pattern of these details.

If you use a Fast Stable Diffusion environment, which I recommend above, all of these details (an even more other ControlNet models) are already in the environment, with the exception of IP Adapters.
You can use the following [script to download and deploy IP adapters](py/sd_deploy.py).
Please fix the destination folder in the script before running it.

#### Optional SD components

1. ControlNet reference_only. It can also be used to add a reference image, but the IP Adapter Plus usually gives better results.
2. LoRA models. This is a perfect way to keep generation consistent, but it requires some additional work to create LoRA.
If you plan to use neural art regularly (which in my opinion is absolutely necessary today), please study LoRA technology and create and use your own LoRA models.
3. Inpainting SD models (for example, a [model from Runway](https://huggingface.co/runwayml/stable-diffusion-inpainting/resolve/main/sd-v1-5-inpainting.ckpt)).
This often results in a really smooth and high-quality blend of textures, but usually the image is blurred and lacks interesting detail.
4. Custom SD models. Typically, neural artists use such models, but not original SD 1.5 or SDXL because custom models are based on original models, 
but created later and created by neural artists that use it and so contains knowledge important for practical tasks.
However, I don’t yet have information about how good these models are specifically for texturing, so I can recommend none of them as a required.
I hope that soon we will see new models that are more focused on texturing. 





