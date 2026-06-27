async function clearCache() {
    const cacheNames = await caches.keys();

    await Promise.all(
        cacheNames.map(name => caches.delete(name))
    );

    const registrations = await navigator.serviceWorker.getRegistrations();

    for (const registration of registrations) {
        await registration.unregister();
    }

    window.location.reload();
}