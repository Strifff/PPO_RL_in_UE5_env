import unreal
import torch

from unreal import EditorLevelLibrary

editor_subsystem = unreal.get_editor_subsystem(unreal.UnrealEditorSubsystem)

# Use the new method to get the editor world
editor_world = editor_subsystem.get_editor_world()

# Now you can continue with your operations using editor_world
print(editor_world)


print("halli hallå")
