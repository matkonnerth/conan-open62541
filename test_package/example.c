#include <open62541/server.h>
#include <open62541/server_config_default.h>

int main()
{
    UA_Server* server = UA_Server_new();
    UA_Server_delete(server);
}
