from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()

from open_webui.models.promptusages import (
    PromptUsageModel,
    PromptUsages,
)

from open_webui.constants import ERROR_MESSAGES
from open_webui.utils.auth import get_verified_user
from open_webui.utils.access_control import has_access

############################
# GetPromptUsageByCommand
############################

@router.get("/{command}/usage")
async def get_usage_by_command(command: str, user=Depends(get_verified_user)):
    promptusage = PromptUsages.get_usage_by_command(f"/{command}")

    if promptusage:
        if user.role == "admin":
            return promptusage.uses
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=ERROR_MESSAGES.NOT_FOUND,
        )