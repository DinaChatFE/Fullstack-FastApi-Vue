import fastapi
from fastapi.exceptions import HTTPException
from pony.orm import commit
import crud
from starlette.requests import Request
import schemas
from typing import List

category_route = fastapi.APIRouter(prefix="/category", tags=['Category'])


@category_route.post('/', response_model=schemas.CategoryOut)
def write_data(schema: schemas.CreateCategory,
               request: Request,
               current_user=fastapi.Depends(
                   crud.user_crud.authenticate_by_token)):
    with request.pony_session:
        category = crud.category_crud.model(**schema.dict())
        commit()
        category.flush()
        return category


@category_route.get('/', response_model=List[schemas.CategoryOut])
def read_data(request: Request):
    with request.pony_session:
        return list(crud.category_crud.get_multi())


@category_route.get('/{id}', response_model=schemas.CategoryOut)
def read_one_data(request: Request,
                  id: int,
                  current_user=fastapi.Depends(
                      crud.user_crud.authenticate_by_token)):
    with request.pony_session:
        model = crud.category_crud.model.get(id=id)
        if not model:
            raise HTTPException(status_code=404, detail="Not found")
        return model


@category_route.delete('/{id}')
def delete_data(request: Request,
                  id: int,
                  current_user=fastapi.Depends(
                      crud.user_crud.authenticate_by_token)):
    with request.pony_session:
        model = crud.category_crud.model.get(id=id)
        if not model:
            raise HTTPException(status_code=404, detail="Not found")
        model.delete()
        return {"message": "Deleted successfully"}


@category_route.put('/{id}', response_model=schemas.CategoryOut)
def update_data(request: Request,
                id: int,
                schema: schemas.CreateCategory,
                current_user=fastapi.Depends(
                    crud.user_crud.authenticate_by_token)):
    with request.pony_session:
        model = crud.category_crud.model.get(id=id)
        print(model)
        model.set(**schema.dict())
        commit()
        model.flush()
        return model
