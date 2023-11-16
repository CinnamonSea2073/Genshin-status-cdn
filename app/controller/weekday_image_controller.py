from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter(prefix="/weekday", tags=["weekday images"])


@router.post("/{day_of_week}/")
def get_weekday_image(day_of_week:str = "Monday"):
    filename = f"{day_of_week}.jpg"
    filepath = f"image/weekday/{filename}"
    return FileResponse(filepath, filename=filename)