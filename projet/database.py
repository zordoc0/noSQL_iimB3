from connectDb import connectDb
from seeder import seeder_users, seeder_teams, seeder_projects
from get.get import get_item_by_attr
from update.update import update_item_by_attr, update_item_by_pid
from create.create import create_item, create_items
from delete.delete import delete_item_by_attr, delete_item_by_pid, delete_items_by_attr, delete_items_by_pids
from array.array import array_push_item_by_attr , array_push_item_by_pid, array_pull_item_by_attr, array_pull_item_by_pid
from get.getAdvanced import get_items


dbname = "rendu_b3_iim"

db = connectDb(dbname)

