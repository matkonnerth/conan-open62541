#include <open62541/server.h>
#include <open62541/server_config_default.h>

int main()
{
  UA_Server *server = UA_Server_new();
  UA_ServerConfig_setDefault(UA_Server_getConfig(server));
  UA_Server_run_startup(server);
  UA_Server_run_shutdown(server);
  UA_Server_delete(server);
}
