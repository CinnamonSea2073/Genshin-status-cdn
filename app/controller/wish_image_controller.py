from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter(prefix="/wish", tags=["wish images"])


@router.post("/banner/character/{banner_id}/")
def get_wish_banner_character_image(banner_id:int = 0):
    filename = f"{banner_id}.jpg"
    filepath = f"image/wish/banner/{filename}"
    return FileResponse(filepath, filename=filename)

@router.post("/screen/character/{rarity}/{character_name}")
def get_wish_screen_character_image(rarity:int = 4, character_name:str = "アンバー"):
    filename = f"{character_name}.jpg"
    filepath = f"image/wish/screen/character/{rarity}/{filename}"
    return FileResponse(filepath, filename=filename)

@router.post("/screen/weapon/{rarity}/{weapon_name}")
def get_wish_screen_weapon_image(rarity:int = 3, weapon_name:str = "シャープシューターの誓い"):
    filename = f"{weapon_name}.jpg"
    filepath = f"image/wish/screen/weapon/{rarity}/{filename}"
    return FileResponse(filepath, filename=filename)