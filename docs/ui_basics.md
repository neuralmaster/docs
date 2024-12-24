
## UI lauout

When the new Neural Master session is initialized in blender file it creates a new UI layout (also named workspace) witch has name Neural Mater and contains several areas convenient to work with this tool.
Layout contains 4 areas:

![UI layout](img/ui_layout.png)

1. Main 3d view area, showing the rendered image from the main camera of Neural Master.  
   When Neural Master pass some operations it can automatically switch the mode of this area.
2. Additional 3d view area is intended for moving and tuning the main camera and also other different operation if it is required. Neural Master does not influence the view of this area. 
3. Image Editor is used for viewing and editing different images used by Neural Master, for example for editing inpaint masks.
4. Shading Editor. This area is formally required for some Blender operator used by Neural Master. If you hide this area then some operations will not work. 
   (But don't worry you don't need to edit shaders to work with the tool).  

## UI panels

User interacts with Neural Master by using several UI panels

1. Neural Master Control panel displays in the 3d view areas, and it must be used in the main 3d view area.  
2. Neural Master Settings panel contains a lot of different settings for the tool and it can be used in the main and additional 3d view areas.  
3. Neural Master Painting panel contains tools for painting masks and textures and it can be used in image editor area.  

To open Control panel and Master Settings press N button when the mouse cursor is in 3d view area and then press Neural Master tab and then open "Neural Master Control" panel.
To open Painting panel do the same in Image Editor area.

## UI subpanels

Every UI panel contains several "subpanels" for convenient work with the tool.

To avoid inconvenience extra prefix we will use the term "panel" instead of "UI panel" in the description bellow.

### Subpanels list

1. Subpanels of the Neural Master Control panel:

    - [Create new session](panels/create_session_panel.md)
    - [Open session](panels/open_session_panel.md)
    - [Texure layers](panels/layers_panel.md)
    - [Camera coontrol](panels/camera_panel.md)
    - [Main control](panels/main_control_panel.md)
    - [Render settings](panels/render_settings_panel.md)

2. Subpanels of the Neural Master Settings panel:

    - [SD connection](panels/sd_connection_panel.md)
    - [SD settings](panels/sd_settings_panel.md)
    - [ControlNet](panels/sd_controlnet_panel.md)
    - [Player](panels/player_panel.md)
    - [Debug](panels/debug_panel.md)

3.  Subpanels of the Neural Master Painting panel:

    - [Inpaint settings](panels/inpaint_settings_panel.md) (new)
    - [Inpaint tools](panels/inpaint_tools_panel.md) (new)

### Subpanels structure

All the subpanels have the same structure and contains 5 elements that we can see on the image bellow

![Render settings panel](img/render_settings_panel.img)

1. Title contain the title name of the subpanel
2. Collapse/expand button. The subpanel can be collapsed/expander using this button. 
3. Question button witch takes you to the documentation page corresponding to this subpanel
4. Main appears if the subpanel expanded, and it contains all the UI valuable elements of the subpanel.
5. Error indicator exists if there is any error in teh settings of panel. Expand the subpanel to find the details of the error.


## Addon settings 

## Notes

1. We recommend you to use UI layout Neural Master to work with the tool, because we tried to make it convenient for work. However, you can use another layout as long as it has at least one 3d view area, one 2d area and one shader editor area.
2. Please do not edit shaders of Neural Master during the work (despite the fact that there is a shader editor) because iе can corrupt the result.  
3. When you press control buttons in Neural Master Control panel it call different operation including switching the mode of the 3d area where this panel is located. That's why we recommend you to use this panel in main 3dview area as described above.    


