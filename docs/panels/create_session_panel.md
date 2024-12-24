# Neural Master Session Initialization Panel

This panel is assists in setting up a new texturing session. It accommodates two distinct scenarios depending on the starting point of your texturing process:

- For a mesh without an initial texture, use the "Use Color" mode.
- For a mesh with an existing texture that you wish to enhance, select the "Use Texture+UV" mode.

## Common UI Elements

Regardless of the mode, you'll encounter these common elements:

1. **Choose Mesh**: A dropdown menu for selecting the mesh that will be textured.
2. **How to initialize the texture?**: A dropdown menu providing two initialization methods for the texture:
   - **Use Color**: Initializes the texture with a uniform color.
   - **Use Texture+UV**: Initializes the texture based on an existing texture map and corresponding UV layout.
3. **Select Destination UV**: A dropdown for selecting the UV map that the final texture will use. This UV map is also utilized for creating texture layer masks within NeuralMaster.

**Notes:**

- The Destination UV Map must be non-overlapping to ensure the correct creation of the texture.
- The Destination UV Map and mesh are not required to be in their final forms. You can perform further refinements such as subdividing the mesh or adding details during the NeuralMaster session.

## "Use Color" Mode

![Control Panel - Use Color Mode](../img/create_session_color.png)

Opt for the "Use Color" mode when starting without any pre-existing texture.  
This mode allows you to fill the object with a chosen color, which acts as the base for subsequent texturing.
By default, this is set to black, but you can select any color that suits your project's needs.

## "Use Texture+UV" Mode

![Control Panel - Use Texture + UV Mode](../img/create_session_texture.png)

The "Use Texture+UV" mode is ideal for refining an existing texture or working from a preliminary texture map.  
This mode requires you to select both the texture image you wish to improve and its associated UV map.
Note that the source UV map can differ from the final one and may have overlapping areas.


After setting up the panel according to your needs click **Start new session** to begin the texturing process with NeuralMaster.
