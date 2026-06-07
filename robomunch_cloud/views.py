import base64
import io

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from PIL import Image


@csrf_exempt
@require_http_methods(["POST"])
def get_resolution(request):
    """Returns the resolution of the received image."""
    try:
        import json
        data = json.loads(request.body)
        image_b64 = data.get("image", "")
        if not image_b64:
            return JsonResponse({"error": "No image provided."}, status=400)

        image_bytes = base64.b64decode(image_b64)
        image = Image.open(io.BytesIO(image_bytes))
        width, height = image.size

        return JsonResponse({
            "width": width,
            "height": height,
            "resolution": f"{width}x{height}",
        })
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
@require_http_methods(["POST"])
def convert_grayscale(request):
    """Converts the received image to grayscale and returns it."""
    try:
        import json
        data = json.loads(request.body)
        image_b64 = data.get("image", "")
        if not image_b64:
            return JsonResponse({"error": "No image provided."}, status=400)

        image_bytes = base64.b64decode(image_b64)
        image = Image.open(io.BytesIO(image_bytes))
        grayscale = image.convert("L")

        buf = io.BytesIO()
        grayscale.save(buf, format="PNG")
        result_b64 = base64.b64encode(buf.getvalue()).decode("utf-8")

        return JsonResponse({"image": result_b64})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
