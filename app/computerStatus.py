import urllib3
import deepsecurity as ds
from deepsecurity.rest import ApiException
import sqlite3


def init_db():
    sql_conn = sqlite3.connect("computers.db")
    c = sql_conn.cursor()

    c.execute(
        """CREATE TABLE computers (
        hostname text, 
        agent_present int,
        agent_status text,
        agent_status_messages text,
        agent_tasks text, 
        agent_version text, 
        platform text
        )"""
    )
    sql_conn.commit()
    sql_conn.close()
    print(f"init_db complete")


def gather_computers(api_config):
    # Basic API Setup
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    api_version = "v1"
    expand = ds.Expand(ds.Expand.computer_status)

    # Search Criteria
    search_criteria = ds.SearchCriteria()
    search_criteria.id_value = 0
    search_criteria.id_test = "greater-than"

    # Search Filter
    page_size = 5000
    search_filter = ds.SearchFilter()
    search_filter.max_items = page_size
    search_filter.search_criteria = [search_criteria]

    # Based off: https://automation.deepsecurity.trendmicro.com/article/20_0/how-to-search/#limit-search-results-and-paging
    computers_api = ds.ComputersApi(ds.ApiClient(api_config))
    paged_computers = []
    while True:
        computers = computers_api.search_computers(
            api_version,
            search_filter=search_filter,
            expand=expand.list(),
            overrides=False,
        )
        num_found = len(computers.computers)
        current_paged_computers = []

        if num_found == 0:
            print(f"No computers found.")
            break

        for computer in computers.computers:
            current_paged_computers.append(computer)

        paged_computers.append(current_paged_computers)

        # Get the ID of the last computer in the page and return it with the number of computers on the page
        last_id = computers.computers[-1].id
        search_criteria.id_value = last_id
        print("Last ID: " + str(last_id), "Computers found: " + str(num_found))
    return paged_computers


def computer_load(paged_computers):
    init_db()
    for computer_list in paged_computers:
        sql_conn = sqlite3.connect("computers.db")
        c = sql_conn.cursor()
        for computer in computer_list:
            hostname = computer.host_name
            # Computers with no agent
            if computer.agent_finger_print is None:

                # Set values so they're not empty
                agent_present = 0
                agent_status = "N/A"
                agent_status_messages = "N/A"
                agent_tasks = "N/A"
                agent_version = "N/A"
                platform = "N/A"

                # Set values if present
                if (
                    computer.computer_status is not None
                    and computer.computer_status.agent_status is not None
                ):
                    agent_status = computer.computer_status.agent_status
                    agent_status_messages = str(
                        computer.computer_status.agent_status_messages
                    )

            else:
                agent_present = 1
                platform = computer.platform
                agent_status = computer.computer_status.agent_status
                agent_version = computer.agent_version

                # Agent Status
                if computer.computer_status.agent_status is not None:
                    agent_status = computer.computer_status.agent_status
                else:
                    agent_status = "N/A"

                # Agent Status Messages
                if computer.computer_status.agent_status_messages is not None:
                    agent_status_messages = str(
                        computer.computer_status.agent_status_messages
                    )
                else:
                    agent_status_messages = "N/A"

                # Agent Tasks
                if computer.tasks is not None:
                    agent_tasks = str(computer.tasks.agent_tasks)
                else:
                    agent_tasks = "N/A"

            # SQL Query to load computers into DB
            c.execute(
                "INSERT INTO computers VALUES(?, ?, ?, ?, ?, ?, ?);",
                (
                    hostname,
                    agent_present,
                    agent_status,
                    agent_status_messages,
                    agent_tasks,
                    agent_version,
                    platform,
                ),
            )
        sql_conn.commit()
        sql_conn.close()
    print(f"Computers added to DB")


def get_count():
    sql_conn = sqlite3.connect("computers.db")
    c = sql_conn.cursor()
    c.execute("SELECT * FROM computers")
    print(len(c.fetchall()))
    sql_conn.commit()
    sql_conn.close()


def get_rows():
    sql_conn = sqlite3.connect("computers.db")
    c = sql_conn.cursor()
    c.execute("SELECT * FROM computers")
    print(c.fetchall())
    sql_conn.commit()
    sql_conn.close()
