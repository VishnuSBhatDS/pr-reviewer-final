from context import generate_java_context

context = generate_java_context(
    repo="/Users/dealshare/Downloads/cart-service",
    files=["src/main/java/com/dealshare/service/cartservice/services/CartConfigService.java"],
    reverse_limit=10,
    include_tests=False,
    return_string=False,
    output="context_full_programmatical.txt"
)

