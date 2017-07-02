# Django REST framework
URL : <a href="http://www.django-rest-framework.org/">www.django-rest-framework.org</a>

## 질문리스트
* REST framework의 request instance 와 Django의 HttpRequest의 차이점이 뭔지 잘 모르겠음
* 역시 REST framework Response와 Django의 HttpResponse의 차이점도 잘 모르겠음
* 엔드포인트?
* 



## Request object
### Request.data
> request.data는 요청내용을 파싱된 형태로 반환한다.(보통 딕셔너리형태로) cf)request.POST, request.FILE과 비슷하다.
> 
> POST요청 외에도 PUT이나 PATCH같은 요청을 구분하여 접근할 수 있다.
> 
> form데이터를 가지고 JSON형식으로 처리했던 것처럼 가공할 수 있도록 지원해 준다.

### Request.query_params
> request.GET과 흡사하다.
> 
> 하지만 request.GET을 사용하는 것보다 코드를 명확하고 간결하게 짤 수 있도록 도와준다.

### Request.parsers
> APIView나 @api_view데코레이터에 정의되어 있고, Parser 인스턴스를 만들어 준다.
> 
> 파서가 필요한 이유는 많은 클라이언트 요청들이 정형화되지 않은 내용들을 request.data에 싣어보내는데, 이때 보통은 에러를 발행시킨다.


## Authentication
* API의 부분부분마다 다른 인증정책을 쓸 수 있고
* 복합적인 인증정책을 사용할 수 있고
* 들어오는 요청에 관련된 유저와 토큰정보에 제공될 수 있다.

### .user
> 보통은 django.contrib.auth.models.User 경로의 유저 인스턴스를 반환한다. 기본값은 django.contrib.auth.models.AnonymousUser 이다.

### .auth
> 추가적인 인증 context를 반환 할 수 있다.
> 
> APIView나 @api_view데코레이터에 정의되어 있고, Authentication 인스턴스를 만들어준다.

## Browser enhancements
> REST framework는 POST요청 이외에도 브라우저 베이스의 PUT 이나 PATCH, DELETE 요청을 사용할 수 있도록 해준다.

### .method
> html from 테그의 data-method로 사용가능 > PUT, FATCH, DELETE가 있음
>

### .content_type
>non-form content 데이터에 직접 접근해야하는 미디어 타입의 경우 사용 - string 오브젝트를 반환

### .stream
>stream으로 반환


## Response - TemplateResponse object
여러 콘텐츠 형식으로 렌더링이 가능한 Response 클래스~

### Reponse()로 생성
> Response(data, status=None, template_name=None, headers=None, content_type=None)

* data: The serialized data for the response.
* status: A status code for the response. Defaults to 200.
* template_name: A template name to use if HTMLRenderer is selected.
* headers: A dictionary of HTTP headers to use in the response.
* content_type: The content type of the response. Typically, this will be set automatically by the renderer as determined by content negotiation, but there may be some cases where you need to specify the content type explicitly. 

#### attribute
* Resoponse().data - 랜더링되지 않은 Request 오브젝트 반환
* 딕셔너리로 바로 변환하는 것은 .render(data, accepted_media_type, renderer_context)