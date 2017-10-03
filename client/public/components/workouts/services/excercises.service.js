workouts
    .factory('Excercises', function($resource) {
        return $resource(
            'http://127.0.0.1:8000/excercises/',
            {},
            {
                'query': {
                    method: 'GET',
                    isArray: true,
                    headers: {
                        'Content-Type':'application/json'
                    }
                }
            },
            {
                stripTrailingSlashes: false
            }
        );
    });