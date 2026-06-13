- парсер парсит OpenAPI
- помещает в OpenAPISpec
- опенапи спек парсится на много APIResource
- они помещаются в APIResourcesBundle
- дальше APIResourceBundle разбирается асинхронными джобами по APIResource энтитям 
- и отправляются в нейронку
- нейронка генерит по ресурсу код контроллера и отдаёт
- код помещается в VO CodeContent и затем в ControllerResource
- короче дальше то же самое с вьюхами (темплейтами), 
- затем инпут сущность (APIResource), полученная сущность ControllerResource, ViewResource собираются в MVCResource 
- и в MVCResourcesBundle. 

Понятно, что в каждом отдельном MVCResource -> ControllerResource -> CodeContent будут импорты из соседних ресурсов либо что-то такое. 

- интеграционная валидация далее