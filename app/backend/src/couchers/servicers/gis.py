import json
import logging

from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.sql import func

from couchers.db import session_scope
from couchers.models import Node, Page, PageType, PageVersion, User
from couchers.sql import couchers_select as select
from proto import gis_pb2_grpc
from proto.google.api import httpbody_pb2

logger = logging.getLogger(__name__)


def _build_geojson_select(statement):
    """
    See usages below.
    """
    # this is basically a translation of the postgis ST_AsGeoJSON example into sqlalchemy/geoalchemy2
    return func.json_build_object(
        "type",
        "FeatureCollection",
        "features",
        func.json_agg(func.ST_AsGeoJSON(statement.subquery(), maxdecimaldigits=5).cast(JSON)),
    )


def _statement_to_geojson_response(session, statement):
    json_dict = session.execute(select(_build_geojson_select(statement))).scalar_one_or_none()
    return httpbody_pb2.HttpBody(
        content_type="application/json",
        # json.dumps escapes non-ascii characters
        data=json.dumps(json_dict).encode("ascii"),
    )


class GIS(gis_pb2_grpc.GISServicer):
    def GetUsers(self, request, context):
        with session_scope() as session:
            statement = select(User.username, User.id, User.geom).where_users_visible(context).where(User.geom != None)

            return _statement_to_geojson_response(session, statement)

    def GetCommunities(self, request, context):
        with session_scope() as session:
            statement = select(Node).where(Node.geom != None)

            return _statement_to_geojson_response(session, statement)

    def GetPlaces(self, request, context):
        with session_scope() as session:
            # need to do a subquery here so we get pages without a geom, not just versions without geom
            latest_pages = (
                select(func.max(PageVersion.id).label("id"))
                .join(Page, Page.id == PageVersion.page_id)
                .where(Page.type == PageType.place)
                .group_by(PageVersion.page_id)
                .subquery()
            )

            statement = (
                select(PageVersion.page_id.label("id"), PageVersion.slug.label("slug"), PageVersion.geom)
                .join(latest_pages, latest_pages.c.id == PageVersion.id)
                .where(PageVersion.geom != None)
            )

            return _statement_to_geojson_response(session, statement)

    def GetGuides(self, request, context):
        with session_scope() as session:
            latest_pages = (
                select(func.max(PageVersion.id).label("id"))
                .join(Page, Page.id == PageVersion.page_id)
                .where(Page.type == PageType.guide)
                .group_by(PageVersion.page_id)
                .subquery()
            )

            statement = (
                select(PageVersion.page_id.label("id"), PageVersion.slug.label("slug"), PageVersion.geom)
                .join(latest_pages, latest_pages.c.id == PageVersion.id)
                .where(PageVersion.geom != None)
            )

            return _statement_to_geojson_response(session, statement)
