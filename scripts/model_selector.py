"""
Multi-Model Selector - Pilih model paling caem
"""

MODEL_CONFIGS = {
    "person": {
        "primary_model": "gradients-io-tournaments/Qwen-Image-Jib-Mix",
        "backup_model": "gradients-io-tournaments/Z-Image-Turbo",
        "model_type": "qwen-image",
        "recipe": "qwen_person.json",
        "trigger_word": "person_subject"
    },
    "style": {
        "primary_model": "dataautogpt3/ProteusSigma",
        "backup_model": "Lykon/dreamshaper-xl-1-0",
        "model_type": "sdxl",
        "recipe": "sdxl_style.json",
        "trigger_word": "artstyle"
    },
    "concept": {
        "primary_model": "dataautogpt3/DynaVisionXL",
        "backup_model": "cagliostrolab/animagine-xl-4.0",
        "model_type": "sdxl",
        "recipe": "sdxl_concept.json",
        "trigger_word": "concept_art",
        "anti_overfit": True,
        "early_stopping_patience": 5,
        "validation_split": 0.1
    },
    "sculpture": {
        "primary_model": "dataautogpt3/ProteusSigma",
        "backup_model": "gradients-io-tournaments/Qwen-Image-Jib-Mix",
        "model_type": "sdxl",
        "recipe": "sdxl_sculpture.json",
        "trigger_word": "sculpture"
    }
}

DEFAULT_CONFIG = MODEL_CONFIGS["person"]


def get_model_config(dataset_type: str) -> dict:
    """Get model configuration for detected dataset type."""
    config = MODEL_CONFIGS.get(dataset_type, DEFAULT_CONFIG)
    print(f"Selected model config: primary={config['primary_model']}, type={config['model_type']}")
    return config


def get_recipe_path(recipe_name: str) -> str:
    """Get full path to recipe file."""
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, "lrs", recipe_name)
