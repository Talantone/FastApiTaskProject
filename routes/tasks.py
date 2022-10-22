from typing import List

from fastapi import APIRouter, Depends, Response, HTTPException

from core.current_user import current_user
from models.tasks import Task, TaskUpdate, TaskCreate
from models.user import User

router = APIRouter(prefix='/tasks', tags=["Tasks"])


@router.get("", response_model=List[Task])
async def get_users_tasks(user: User = Depends(current_user)):
    tasks = await Task.find(Task.user.name == user.name).to_list()
    return tasks


@router.get("", response_model=Task)
async def get_task(id: str, user: User = Depends(current_user)):
    task = await Task.find_one(Task.id == id)
    if task.user.name != user.name:
        return Response(status_code=403)
    return task


@router.post("", response_model=Task)
async def create_task(task: TaskCreate, user: User = Depends(current_user)):
    new_task = Task(title=task.title, user=user)
    await new_task.create()
    return new_task


@router.patch("", response_model=Task)
async def update_task(id: str, update: TaskUpdate, user: User = Depends(current_user)):
    task = await Task.find_one(Task.id == id)
    if task.user.name != user.name:
        return Response(status_code=403)
    task = task.copy(update=update.dict(exclude_unset=True))
    await task.save()
    return task


@router.delete("")
async def delete_task(title: str, user: User = Depends(current_user)):
    await Task.find_one(Task.title == title, Task.user.name == user.name).delete()
    return Response(status_code=204)
