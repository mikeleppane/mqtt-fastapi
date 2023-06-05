def test_health_check(test_app):
    """
    GIVEN
    WHEN health check endpoint is called with GET method
    THEN response with status 200 and body OK is returned
    """

    response = test_app.get("/v1/health_check")
    assert response.status_code == 200
    assert response.json() == {"message": "OK"}
