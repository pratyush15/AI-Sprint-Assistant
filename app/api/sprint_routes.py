from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from app.database.db import get_db

from app.services.sprint_service import (
    generate_sprint_summary, 
    generate_sprint_readiness, 
    generate_sprint_risk, 
    generate_sprint_report, 
    generate_sprint_capacity, 
    get_workload_analysis
)

router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)


@router.get("/sprint-summary")
def sprint_summary(
    db: Session = Depends(get_db)
):

    summary = generate_sprint_summary(db)

    return {
        "summary": summary
    }
    
    
@router.get("/sprint-readiness")
def sprint_readiness(
    db: Session = Depends(get_db)
):

    result = generate_sprint_readiness(db)

    return {
        "readiness": result
    }  
    
    
@router.get("/sprint-risk")
def sprint_risk(
    db: Session = Depends(get_db)
):

    risk = generate_sprint_risk(db)

    return {
        "risk": risk
    } 
    
    
@router.get("/sprint-report")
def sprint_report(
    db: Session = Depends(get_db)
):

    pdf = generate_sprint_report(db)

    return StreamingResponse(
        pdf,
        media_type="application/pdf",
        headers={
            "Content-Disposition":
            "attachment; filename=sprint_report.pdf"
        }
    )
    
    
@router.get("/sprint-capacity")
def sprint_capacity(
    db: Session = Depends(get_db)
):

    result = generate_sprint_capacity(db)

    return {
        "capacity": result
    }  
    
    
@router.get("/workload")
def workload(
    db: Session = Depends(get_db)
):

    return get_workload_analysis(db)