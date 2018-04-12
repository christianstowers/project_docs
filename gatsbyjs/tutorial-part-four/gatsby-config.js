module.exports = {
	siteMetadata: {
		title: 'PANDAS EATING DONUTS',
	},
	plugins: [
		{
			resolve: 'gatsby-source-filesystem',
			options: {
				name: 'src',
				path: `${__dirname}/src/`,
			},
		},
		'gatsby-transformer-remark',
		'gatsby-plugin-glamor',
		{
			resolve: 'gatsby-plugin-typography',
			options: {
				pathtoConfigModule: 'src/utils/typography',
			},
		},
	],
};