import requests
import comfy

class EVRstatus:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"url": ("STRING", {"default": ""}), "images": ("IMAGE", ), "body": ("DICT",)}}

    RETURN_TYPES = ("INT", )
    RETURN_NAMES=("status_code",)
    FUNCTION = "send_post_message"

    OUTPUT_NODE = True

    CATEGORY = "EVR/HTTP"
        
    def send_post_message(self, url, body, images):
            response = requests.post(url, json=body)
            print(response, response.status_code, response.text)
            return (response.status_code,)

class EVR_EmptyDictNode:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {}}
    RETURN_TYPES = ("DICT", )
    RETURN_NAMES=("dict",)
    FUNCTION = "execute"
    CATEGORY = "EVR/HTTP"

    def execute(self):
        return ({},)

class EVR_AssocStrNode:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"dict": ("DICT",), "key": ("STRING", {"default": ""}), "value": ("STRING", {"default": ""})}}
    RETURN_TYPES = ("DICT", )
    RETURN_NAMES=("dict",)
    FUNCTION = "execute"
    CATEGORY = "EVR/HTTP"

    def execute(self, dict, key, value):
        return ({**dict, key: value},)


NODE_CLASS_MAPPINGS = {
    "EVR-status": EVRstatus,
    "EVR-EZEmptyDictNode": EVR_EmptyDictNode,
    "EVR-EZAssocStrNode": EVR_AssocStrNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "EVR-status": "HTTP POST",
    "EZEmptyDictNode": "Empty Dict",
    "EZAssocStrNode": "Assoc Str",
}
