# # --- НАЧАЛО ТЕСТИРОВАНИЯ ШАГА 2 ---
# bundle_repo = container.resolve(BaseAPIResourcesBundleRepository)

# # 1. Настраиваем и запускаем фоновый воркер
# from logic.worker import run_specs_worker
# await run_specs_worker(broker=message_broker, mediator=mediator)

# # 2. Так как наш MemoryMessageBroker при вызове send_message в Шаге 1
# # сразу же триггерит подписчиков, цепочка Шага 2 уже должна выполниться!

# # 3. Проверяем, что бандл ресурсов создался и сохранился в репозиторий
# all_bundles = list(await bundle_repo.get_all_items(filters=any_filter_or_mock))
# assert len(all_bundles) == 1, "Бандл ресурсов должен автоматически создаться воркером"

# saved_bundle = all_bundles[0]
# assert saved_bundle.spec_oid == returned_spec.oid
