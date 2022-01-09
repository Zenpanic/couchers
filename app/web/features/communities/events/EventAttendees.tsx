import { useState } from "react";
import { useTranslation } from "react-i18next";

import EventAttendeesDialog from "./EventAttendeesDialog";
import EventUsers from "./EventUsers";
import { useEventAttendees } from "./hooks";

interface EventAttendeesProps {
  eventId: number;
}

export default function EventAttendees({ eventId }: EventAttendeesProps) {
  const { t } = useTranslation(["communities"]);
  const {
    attendees,
    attendeesIds,
    error,
    isLoading,
    isAttendeesRefetching,
    hasNextPage,
  } = useEventAttendees({ eventId, type: "summary" });

  const [isDialogOpen, setIsDialogOpen] = useState(false);
  return (
    <>
      <EventUsers
        emptyState={t("communities:no_attendees")}
        error={error}
        hasNextPage={hasNextPage}
        isLoading={isLoading}
        isUsersRefetching={isAttendeesRefetching}
        onSeeAllClick={() => setIsDialogOpen(true)}
        users={attendees}
        userIds={attendeesIds}
        title={t("communities:attendees")}
      />
      <EventAttendeesDialog
        eventId={eventId}
        open={isDialogOpen}
        onClose={() => setIsDialogOpen(false)}
      />
    </>
  );
}