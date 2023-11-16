from fastapi import FastAPI
import controller.weekday_image_controller as image_ctrl
import controller.wish_image_controller as status_ctrl

app = FastAPI()


app.include_router(image_ctrl.router)
app.include_router(status_ctrl.router)