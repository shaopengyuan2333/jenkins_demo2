from django.utils.deprecation import MiddlewareMixin


class CoreMiddle(MiddlewareMixin):
    def process_response(self, request, response):
        if request.method == 'OPTIONS':
            response['Access-Control-Allow-Headers'] = 'Content-Type, authorization'  # 如果是 * 就代表全部IP都可以访问
        response['Access-Control-Allow-Origin'] = '*'
        return response