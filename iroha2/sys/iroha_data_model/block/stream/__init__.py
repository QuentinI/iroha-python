
from ....rust import make_enum, make_struct, make_tuple, get_class, SelfResolvingTypeVar, Dict
import typing
            
BlockMessage = make_tuple("BlockMessage", ["iroha_data_model.block.committed.VersionedCommittedBlock"])
BlockSubscriptionRequest = make_tuple("BlockSubscriptionRequest", [int])
VersionedBlockMessage = make_enum("VersionedBlockMessage", [("V1", get_class("iroha_data_model.block.stream.BlockMessage"))], typing.Union[get_class("iroha_data_model.block.stream.BlockMessage")])

VersionedBlockSubscriptionRequest = make_enum("VersionedBlockSubscriptionRequest", [("V1", get_class("iroha_data_model.block.stream.BlockSubscriptionRequest"))], typing.Union[get_class("iroha_data_model.block.stream.BlockSubscriptionRequest")])

SelfResolvingTypeVar.resolve_all()
