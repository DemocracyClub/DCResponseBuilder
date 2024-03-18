from response_builder.v1.builders.ballots import (
    StockLocalBallotBuilder, 
)
from response_builder.v1.builders.base import RootBuilder
from response_builder.v1.builders.polling_stations import PollingStationBuilder
from response_builder.v1.generated_responses import electoral_services, polling_stations, candidates

 
# < -- polling stations -- > 
POLLING_STATION = (
    PollingStationBuilder().set("polling_station_known", True).build()
)
POLLING_STATION.station = polling_stations.station


# < -- voting systems -- >
FPTP_VOTING_SYSTEM = RootBuilder().with_ballot(
    StockLocalBallotBuilder().build()).with_voting_system("FPTP")
STV_VOTING_SYSTEM = RootBuilder().with_ballot(
    StockLocalBallotBuilder().build()).with_voting_system("STV")
AMS_VOTING_SYSTEM = RootBuilder().with_ballot(
    StockLocalBallotBuilder().build()).with_voting_system("AMS")
SV_VOTING_SYSTEM = RootBuilder().with_ballot(
    StockLocalBallotBuilder().build()).with_voting_system("sv")

# < -- election types -- >
LOCAL = StockLocalBallotBuilder().build()
GLA = StockLocalBallotBuilder().with_ballot_title("London Assembly elections").with_post_name("London Assembly").with_election_name("London Assembly elections").with_ballot_paper_id("gla.a.2024-05-02").with_election_id("gla.a.2024-05-02").build()
MAYORAL = StockLocalBallotBuilder().with_ballot_title("Mayor of London").with_post_name("Mayor of London").with_election_name("Mayor of London").with_ballot_paper_id("mayor.london.2024-11-02").with_election_id("mayor.london.2024-11-02").build()
PCC = StockLocalBallotBuilder().with_ballot_title("Police and Crime Commissioner elections").with_post_name("Police and Crime Commissioner for Avon and Somerset").with_election_name("Police and Crime Commissioner election").with_ballot_paper_id("pcc.avon-and-somerset.2024-05-02").with_election_id("pcc.avon-and-somerset.2024-05-02").build()
PARL = StockLocalBallotBuilder().with_ballot_title("Stroud Slade parliamentary by-election").with_post_name("Stroud Slade constituency").with_election_name("Stroud Slade constituency").with_ballot_paper_id("parl.stroud.2024-11-14").with_election_id("parl.stroud.2024-11-14").build()

# < -- root responses -- >
NO_LOCAL_BALLOTS = RootBuilder().without_ballot()

# This is a local ballot by default
CANCELLED_BALLOT = RootBuilder().with_ballot(StockLocalBallotBuilder().build()).with_cancelled()

RECENTLY_PASSED_LOCAL_BALLOT = (
    RootBuilder()
    .with_ballot(StockLocalBallotBuilder(
        poll_open_date="2024-03-01",
        ballot_paper_id="local.stroud.2024-03-01",
        
    ).build())
)

SINGLE_LOCAL_FUTURE_BALLOT_WITH_POLLING_STATION = (
    RootBuilder()
    .with_ballot(StockLocalBallotBuilder().build())
    .with_candidates(candidates.all_candidates)
    .with_polling_station(POLLING_STATION)
     .with_electoral_services(electoral_services.stroud_electoral_services)
)

SINGLE_LOCAL_FUTURE_BALLOT_WITHOUT_POLLING_STATION = (
    RootBuilder()
    .with_ballot(StockLocalBallotBuilder().build())
    .with_candidates(candidates.all_candidates)
    .without_polling_station()
     .with_electoral_services(electoral_services.stroud_electoral_services)
)

SINGLE_LOCAL_FUTURE_BALLOT_WITH_ADDRESS_PICKER = (
    RootBuilder()
    .with_ballot(LOCAL)
    .with_candidates(candidates.all_candidates)
    .with_address_picker()
    .with_electoral_services(electoral_services.wandsworth_electoral_services)
)

MULTIPLE_BALLOTS_WITH_VOTING_SYSTEM_AND_POLLING_STATION = (
    RootBuilder()
    .with_multiple_ballots([MAYORAL, GLA])
    .with_candidates(candidates.all_candidates)
    .with_voting_system("FPTP")
    .with_polling_station(POLLING_STATION)
    .with_electoral_services(electoral_services.stroud_electoral_services)
)


MULTIPLE_BALLOTS_WITH_CANCELLATION = RootBuilder().with_multiple_ballots(
    [MAYORAL, PARL, GLA, RootBuilder().with_ballot(LOCAL).with_cancelled().build()])

PARL_BALLOT = RootBuilder().with_ballot(
    PARL).with_polling_station(POLLING_STATION).with_electoral_services(electoral_services.stroud_electoral_services)
   
GLA_BALLOT = RootBuilder().with_ballot(
    StockLocalBallotBuilder().build()).with_polling_station(POLLING_STATION).with_electoral_services(electoral_services.wandsworth_electoral_services)

PCC_BALLOT = RootBuilder().with_ballot(
    PCC).with_polling_station(POLLING_STATION).with_electoral_services(electoral_services.stroud_electoral_services)
    
MAYORAL_BALLOT = RootBuilder().with_ballot(
    MAYORAL).with_polling_station(POLLING_STATION).with_electoral_services(electoral_services.wandsworth_electoral_services)
  
CANCELLED_BALLOT = RootBuilder().with_ballot(
    StockLocalBallotBuilder().build()).with_electoral_services(electoral_services.wandsworth_electoral_services).with_voting_system("FPTP").with_cancelled()
