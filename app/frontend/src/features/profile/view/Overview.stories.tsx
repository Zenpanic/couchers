import { Meta, Story } from "@storybook/react";
import Overview, { OverviewProps } from "features/profile/view/Overview";
import users from "test/fixtures/users.json";

export default {
  component: Overview,
  title: "Profile/Overview",
} as Meta;

const Template: Story<OverviewProps> = (args) => <Overview {...args} />;

export const profileOverview = Template.bind({});
profileOverview.args = {
  user: users[0],
};