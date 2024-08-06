import os

import solara
import solara.lab
from dotenv import load_dotenv
import shopify
from agents import create_agent, create_env, create_task

load_dotenv()
shopify_token = os.getenv("SHOPIFY_TOKEN")
shopify_merchant = os.getenv("SHOPIFY_MERCHANT")

api_session = shopify.Session(shopify_merchant, "2021-10", shopify_token)
shopify.ShopifyResource.activate_session(api_session)

orders = ["6207934955610", "6207934988378", "6207935086682", "6207935152218", "6207935348826", "6207935479898", "6207935610970"]
order_no = solara.reactive("6207934955610")

environment = create_env()
agent = create_agent(
    env_id=environment,
    system_prompt="Generate an interactive email for given order to give order status.",
    agent_name="Email Composer",
    agent_persona="Generate Interactive Email"
)


@solara.component
def Page():
    with solara.AppBarTitle():
        solara.Text("Personalized Order Status Email Generator")
    order_number, set_order_number = solara.use_state("")

    def find_order():
        order = shopify.Order.find(order_no.value).attributes
        set_order_number(str(order))

    solara.Select("Enter Order No", value=order_no, values=orders)
    solara.Button(label="Generate", on_click=find_order())
    task = create_task(
        user_id="default_user",
        agent_id=agent,
        session_id="harshit@lyzr.ai",
        message=order_number
    )
    solara.Markdown(task)


