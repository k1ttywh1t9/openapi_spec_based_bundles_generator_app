============================= test session starts ==============================
platform linux -- Python 3.11.13, pytest-9.0.3, pluggy-1.6.0 -- /mnt/c/share/projects/agents_and_llms/frontend_app_openapi_generator/.venv/bin/python
cachedir: .pytest_cache
rootdir: /mnt/c/share/projects/agents_and_llms/frontend_app_openapi_generator
configfile: pyproject.toml
plugins: anyio-4.13.0, langsmith-0.8.9, asyncio-1.4.0, cov-7.1.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 17 items

app/tests/domain/entities/resources/test_api_resources.py::test_api_resource_creation_fields_initialization PASSED [  5%]
app/tests/domain/entities/resources/test_api_resources.py::test_api_resource_title_generation PASSED [ 11%]
app/tests/domain/entities/resources/test_api_resources.py::test_api_resource_creation_triggers_domain_event PASSED [ 17%]
app/tests/domain/entities/resources/test_base_entities.py::test_base_entity_initialization PASSED [ 23%]
app/tests/domain/entities/resources/test_base_entities.py::test_base_entity_equality_and_hash PASSED [ 29%]
app/tests/domain/entities/resources/test_base_entities.py::test_base_entity_event_lifecycle PASSED [ 35%]
app/tests/domain/entities/resources/test_controller_resources.py::test_controller_resource_creation_fields_initialization PASSED [ 41%]
app/tests/domain/entities/resources/test_controller_resources.py::test_controller_resource_creation_triggers_domain_event PASSED [ 47%]
app/tests/domain/entities/resources/test_view_resources.py::test_view_resource_creation PASSED [ 52%]
app/tests/domain/entities/resources/test_view_resources.py::test_mvc_resources_bundle_creation PASSED [ 58%]
app/tests/domain/entities/specs/test_openapi_spec.py::test_openapi_spec_fields_initialization_success PASSED [ 64%]
app/tests/domain/entities/specs/test_openapi_spec.py::test_openapi_spec_creation_triggers_correct_domain_event_success PASSED [ 70%]
app/tests/domain/entities/specs/test_openapi_spec.py::test_openapi_spec_registers_event_in_internal_lifecycle_success PASSED [ 76%]
app/tests/domain/values/test_code_content.py::test_code_content_value_object_creation_success PASSED [ 82%]
app/tests/domain/values/test_code_content.py::test_code_content_value_object_creation_raises_empty_exception PASSED [ 88%]
app/tests/domain/values/test_code_content.py::test_code_content_value_object_creation_raises_syntax_exception PASSED [ 94%]
app/tests/logic/test_parsing_spec.py::test_parse_openapi_spec_to_entity_logic_success FAILED [100%]

=================================== FAILURES ===================================
_______________ test_parse_openapi_spec_to_entity_logic_success ________________

func = <class 'logic.commands.specs.ParseOpenAPISpecToEntityCommandHandler'>

    def getfullargspec(func):
        """Get the names and default values of a callable object's parameters.
    
        A tuple of seven things is returned:
        (args, varargs, varkw, defaults, kwonlyargs, kwonlydefaults, annotations).
        'args' is a list of the parameter names.
        'varargs' and 'varkw' are the names of the * and ** parameters or None.
        'defaults' is an n-tuple of the default values of the last n parameters.
        'kwonlyargs' is a list of keyword-only parameter names.
        'kwonlydefaults' is a dictionary mapping names from kwonlyargs to defaults.
        'annotations' is a dictionary mapping parameter names to annotations.
    
        Notable differences from inspect.signature():
          - the "self" parameter is always reported, even for bound methods
          - wrapper chains defined by __wrapped__ *not* unwrapped automatically
        """
        try:
            # Re: `skip_bound_arg=False`
            #
            # There is a notable difference in behaviour between getfullargspec
            # and Signature: the former always returns 'self' parameter for bound
            # methods, whereas the Signature always shows the actual calling
            # signature of the passed object.
            #
            # To simulate this behaviour, we "unbind" bound methods, to trick
            # inspect.signature to always return their first parameter ("self",
            # usually)
    
            # Re: `follow_wrapper_chains=False`
            #
            # getfullargspec() historically ignored __wrapped__ attributes,
            # so we ensure that remains the case in 3.3+
    
>           sig = _signature_from_callable(func,
                                           follow_wrapper_chains=False,
                                           skip_bound_arg=False,
                                           sigcls=Signature,
                                           eval_str=False)

/home/k17tt17/.pyenv/versions/3.11.13/lib/python3.11/inspect.py:1365: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/home/k17tt17/.pyenv/versions/3.11.13/lib/python3.11/inspect.py:2558: in _signature_from_callable
    return _get_signature_of(init)
           ^^^^^^^^^^^^^^^^^^^^^^^
/home/k17tt17/.pyenv/versions/3.11.13/lib/python3.11/inspect.py:2461: in _signature_from_callable
    sig = _get_signature_of(obj.__func__)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/home/k17tt17/.pyenv/versions/3.11.13/lib/python3.11/inspect.py:2523: in _signature_from_callable
    return _signature_from_function(sigcls, obj,
/home/k17tt17/.pyenv/versions/3.11.13/lib/python3.11/inspect.py:2376: in _signature_from_function
    parameters.append(Parameter(name, annotation=annotation,
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <[AttributeError("'Parameter' object has no attribute '_kind'") raised in repr()] Parameter object at 0x70f7b1ae10c0>
name = 'self', kind = <_ParameterKind.POSITIONAL_OR_KEYWORD: 1>

    def __init__(self, name, kind, *, default=_empty, annotation=_empty):
        try:
>           self._kind = _ParameterKind(kind)
                         ^^^^^^^^^^^^^^^^^^^^
E           RecursionError: maximum recursion depth exceeded

/home/k17tt17/.pyenv/versions/3.11.13/lib/python3.11/inspect.py:2671: RecursionError

The above exception was the direct cause of the following exception:

container = <punq.Container object at 0x70f7b1a68a50>

    @pytest.mark.asyncio
    async def test_parse_openapi_spec_to_entity_logic_success(container: Container):
>       mediator: Mediator = container.resolve(Mediator)
                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^

app/tests/logic/test_parsing_spec.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:475: in _build_impl
    {
.venv/lib/python3.11/site-packages/punq/__init__.py:476: in <dictcomp>
    k: self._resolve_impl(v, resolution_args, context, args.get(k))
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:492: in _build_impl
    result = registration.builder(**args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
app/logic/init_container.py:49: in init_mediator
    [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:535: in resolve
    return self._resolve_impl(service_key, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:529: in _resolve_impl
    return self._build_impl(registration, kwargs, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.11/site-packages/punq/__init__.py:470: in _build_impl
    spec = inspect.getfullargspec(registration.builder)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

func = <class 'logic.commands.specs.ParseOpenAPISpecToEntityCommandHandler'>

    def getfullargspec(func):
        """Get the names and default values of a callable object's parameters.
    
        A tuple of seven things is returned:
        (args, varargs, varkw, defaults, kwonlyargs, kwonlydefaults, annotations).
        'args' is a list of the parameter names.
        'varargs' and 'varkw' are the names of the * and ** parameters or None.
        'defaults' is an n-tuple of the default values of the last n parameters.
        'kwonlyargs' is a list of keyword-only parameter names.
        'kwonlydefaults' is a dictionary mapping names from kwonlyargs to defaults.
        'annotations' is a dictionary mapping parameter names to annotations.
    
        Notable differences from inspect.signature():
          - the "self" parameter is always reported, even for bound methods
          - wrapper chains defined by __wrapped__ *not* unwrapped automatically
        """
        try:
            # Re: `skip_bound_arg=False`
            #
            # There is a notable difference in behaviour between getfullargspec
            # and Signature: the former always returns 'self' parameter for bound
            # methods, whereas the Signature always shows the actual calling
            # signature of the passed object.
            #
            # To simulate this behaviour, we "unbind" bound methods, to trick
            # inspect.signature to always return their first parameter ("self",
            # usually)
    
            # Re: `follow_wrapper_chains=False`
            #
            # getfullargspec() historically ignored __wrapped__ attributes,
            # so we ensure that remains the case in 3.3+
    
            sig = _signature_from_callable(func,
                                           follow_wrapper_chains=False,
                                           skip_bound_arg=False,
                                           sigcls=Signature,
                                           eval_str=False)
        except Exception as ex:
            # Most of the times 'signature' will raise ValueError.
            # But, it can also raise AttributeError, and, maybe something
            # else. So to be fully backwards compatible, we catch all
            # possible exceptions here, and reraise a TypeError.
>           raise TypeError('unsupported callable') from ex
E           TypeError: unsupported callable

/home/k17tt17/.pyenv/versions/3.11.13/lib/python3.11/inspect.py:1375: TypeError
=========================== short test summary info ============================
FAILED app/tests/logic/test_parsing_spec.py::test_parse_openapi_spec_to_entity_logic_success
========================= 1 failed, 16 passed in 9.26s =========================
