from fastapi import APIRouter
from ..models.blog import Blog
from ..schemas.schemas import Schemas
from bson import ObjectId
from config.database import collection

def response_data(data, status, status_code, message):
    return {'status': status, 'status_code': status_code, 'message': message, 'data': data}

blog_router = APIRouter()

@blog_router.get('/blog/list')
async def blog_list():
    blogs = Schemas.blogs_list_serializer(collection.find())
    return response_data(blogs, status=True, status_code=200, message='Blog get successfully!')

@blog_router.get(f'/blog/{id}')
async def get_blog(id: str):
    blog = None
    blog = Schemas.blog_serializer(collection.find_one({'_id': ObjectId(id)}))

    if blog is not None:
        return response_data(blog, status=True, status_code=200, message='Blog get successfully!')
    else:
        return response_data(blog, status=False, status_code=404, message='Blog not found!')



@blog_router.post('/blog/create')
async def create_blog(blog:Blog):
    data = {}
    _id = collection.insert_one(dict(blog))
    if _id.inserted_id:
        data = Schemas.blog_serializer(collection.find_one({'_id': _id.inserted_id}))
        return response_data(data, status=True, status_code=200, message='Blog created successfully!')
    else:
        return response_data(data, status=False, status_code=400, message='Error in creating blog!')


@blog_router.put(f'/blog/edit/{id}')
async def blog_edit(id:str, blog: Blog):
    collection.find_one_and_update({'_id': ObjectId(id)}, {'$set': dict(blog)})
    updated_blog = Schemas.blog_serializer(collection.find_one({"_id": ObjectId(id)}))
    return response_data(updated_blog, status=True, status_code=204, message='Blog is updated successfully!')


@blog_router.delete(f'/blog/delete/{id}')
async def blog_delete(id:str):
    collection.find_one_and_delete({'_id': ObjectId(id)})
    blogs = Schemas.blogs_list_serializer(collection.find())
    return response_data(blogs, status=True, status_code=204, message='Blog deleted successfully!')