// service-worker.js

const CACHE_NAME = 'my-cache-v1';

self.addEventListener('install', function (event) {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(function (cache) {
                console.log('Opened cache');
            })
    );
});

self.addEventListener('fetch', function (event) {
    const url = new URL(event.request.url);

    if (url.origin === 'https://ddragon.leagueoflegends.com') {
        event.respondWith(
            caches.match(event.request)
                .then(function (response) {
                    if (response) {
                        return response;
                    }

                    let fetchRequest = event.request.clone();

                    return fetch(fetchRequest).then(
                        function (response) {
                            if (!response || response.status !== 200 || response.type !== 'basic') {
                                return response;
                            }

                            let responseToCache = response.clone();

                            caches.open(CACHE_NAME)
                                .then(function (cache) {
                                    cache.put(event.request, responseToCache);
                                });

                            return response;
                        }
                    );
                })
        );
    } else {
        event.respondWith(
            fetch(event.request)
                .then(function (response) {
                    return response;
                })
                .catch(function () {
                    return caches.match(event.request);
                })
        );
    }
});
