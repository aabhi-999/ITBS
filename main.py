from fastapi import FastAPI
from routes import buses, bookings, tracking

app = FastAPI(title="ITBS Backend")

# include routers
app.include_router(buses.router, prefix="/buses", tags=["Buses"])
app.include_router(bookings.router, prefix="/bookings", tags=["Bookings"])
app.include_router(tracking.router, prefix="/tracking", tags=["Tracking"])

@app.get("/")
def root():
    return {"message": "Welcome to ITBS Backend 🚍"}
