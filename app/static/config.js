require.config({
  baseUrl: '/static/lib',
  paths: {
    'jquery': 'jquery/dist/jquery',
    'semantic': 'semantic/dist/semantic'
  },
  shim: {
    'semantic': {
        deps: ['jquery']
    }
  }
});
