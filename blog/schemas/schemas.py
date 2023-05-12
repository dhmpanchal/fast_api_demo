class Schemas(object):

    @staticmethod
    def blog_serializer(blog) -> dict:
        print('blog---', blog)
        return {
            'id':str(blog["_id"]),
            'title':blog["title"],
            'body':blog["body"],
            'published':blog["published"]
        }
    
    @staticmethod
    def blogs_list_serializer(blogs) -> list:
        return [Schemas.blog_serializer(blog) for blog in blogs]